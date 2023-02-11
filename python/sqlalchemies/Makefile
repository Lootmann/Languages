run:
	python3 main.py

.PHONY: migrate
migrate:
	python3 -m migrate_db

.PHONY: req
req:
	pip freeze > ./requirements.txt
