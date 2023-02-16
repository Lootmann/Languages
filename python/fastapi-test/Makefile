run:
	PYTHONDONTWRITEBYTECODE=1 python3 -m uvicorn api.main:app --reload --port 8080

test:
	PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -svv

.PHONY: migrate
migrate:
	PYTHONDONTWRITEBYTECODE=1 python3 -m api.migrate_db


.PHONY: pre
pre:
	pre-commit run --all-files
