MANAGE = src/manage.py

requirements:
	pip install -U pip && pip install -r requirements.txt

start:
	 $(MANAGE) runserver 0.0.0.0:8000

mm:
	$(MANAGE) makemigrations

m:
	$(MANAGE) migrate

user:
	$(MANAGE) createsuperuser

lint:
	flake8 ./src

check:
	$(MANAGE) check

check-migrate:
	$(MANAGE) --check --dry-run

shell_plus:
	$(MANAGE) shell_plus --print-sql

celery:
	 cd src && celery -A core worker -l info

beat_celery:
	 cd src && celery -A core beat -l info

flower_celery:
	cd src &&  celery -A core flower

freeze:
	pip freeze > requirements.txt

collect-static:
	python src/manage.py collectstatic

