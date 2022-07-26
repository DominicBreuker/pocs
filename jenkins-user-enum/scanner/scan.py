#!/usr/bin/env python3

import time
import requests


def main():
    target = "http://target:8080"

    for i in range(3):
        print(f"[+] Scanning in {3-i}")
        time.sleep(1)

    if scan(target):
        print(f"[+] Vulnerable target found: {target}")
    else:
        print(f"[+] Target not vulnerable: {target}")


def scan(target: str) -> bool:
    resp = requests.get(f"{target}/asynchPeople/")
    return is_jenkins(resp) and is_vulnerable(resp)


def is_jenkins(resp: requests.Response) -> bool:
    return "X-Jenkins" in resp.headers


def is_vulnerable(resp: requests.Response) -> bool:
    return resp.status_code == 200


if __name__ == "__main__":
    main()
