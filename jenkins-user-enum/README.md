# Jenkins User Enumeration Demo

Jenkins administrators often grant read access to anonymous users.
This allows extracting all users, which may help in follow-up attacks such as password brute-forcing.

This PoC contains a Docker Compose file that will run two containers:
- a `target` which runs a vulnerable Jenkins installation
- a `scanner` which runs a simple Python scan script

Try it out with `make demo` (possibly run `make build`) before to build the containers.
Obviously, you need Docker and Compose installed.


## Simple PoC

Its also possible to check yourself real quick with curl.
Start the containers with `make up`. Jenkins will be on `http://localhost:8080`.
The following PoC can be used to test:

```
curl -sI http://localhost:8080/asynchPeople/ | grep -E '200 OK|X-Jenkins:'
```

## Scanner script

There is a simple Python script in [scanner/scan.py](scanner/scan.py).
This is roughly how it works:

```python
import requests

...

def scan(target: str) -> bool:
    resp = requests.get(f"{target}/asynchPeople/")
    return is_jenkins(resp) and is_vulnerable(resp)


def is_jenkins(resp: requests.Response) -> bool:
    return "X-Jenkins" in resp.headers


def is_vulnerable(resp: requests.Response) -> bool:
    return resp.status_code == 200

...
```


## References

- Jenkins guide on managing access: [Jenkins Docs](https://www.jenkins.io/doc/book/security/managing-security/)
- Metasploit scanner module doing this (and more): [Metasploit Docs](https://www.rapid7.com/db/modules/auxiliary/scanner/http/jenkins_enum/)
