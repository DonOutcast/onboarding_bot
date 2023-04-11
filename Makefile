SOURCE_DIR = src/
PYTHON = python3
TARGET_FILE = manage.py
COMPOSE_FILE = docker-compose.yml

all: build up

migrations:
	$(PYTHON) $(SOURCE_DIR)$(TARGET_FILE) makemigrations

createsuperuserifnotexist:
#	cd src/
#	export DJANGO_SETTINGS_MODULE=onboarding.settings
#	cd ..
	python -c "import sys; \
			import os; \
			os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.onboarding.settings'); \
			import django; \
			django.setup(); \
			from django.contrib.auth.models import User; \
			username='$$DJANGO_SUPERUSER_USERNAME'; \
			email='$$DJANGO_SUPERUSER_EMAIL'; \
			password='$$DJANGO_SUPERUSER_PASSWORD'; \
			User.objects.filter(username=username).exists() or \
			User.objects.create_superuser(username=username, email=email, password=password);"

migrate:
	$(PYTHON) $(SOURCE_DIR)$(TARGET_FILE) migrate

run:
	$(PYTHON) $(SOURCE_DIR)$(TARGET_FILE) runserver 0.0.0.0:8000

web: migrations migrate createsuperuserifnotexist  run

# Команды Docker
build:
	docker-compose -f $(COMPOSE_FILE) build

up:
	docker-compose -f $(COMPOSE_FILE) up -d

down:
	docker-compose -f $(COMPOSE_FILE) down

logs:
	docker-compose -f $(COMPOSE_FILE) logs -f


