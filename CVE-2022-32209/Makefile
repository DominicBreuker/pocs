.PHONY: demo
demo: up show-logs down

.PHONY: build
build:
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: show-logs
show-logs:
	timeout 30 docker-compose logs -f || true
