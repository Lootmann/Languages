run:
	PYTHONDONTWRITEBYTECODE=1 python3 -m uvicorn api.main:app --reload --port 8080

.PHONY: test
test:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -svv

.PHONY: migrate
migrate:
	PYTHONDONTWRITEBYTECODE=1 python3 -m api.migrate_db

.PHONY: docs
docs:
	google-chrome http://127.0.0.1:8080/docs

.PHONY: req
req:
	pip freeze > requirements.txt

.PHONY: pre
pre:
	pre-commit run --all-files
