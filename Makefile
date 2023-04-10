SOURCE_DIR = src/
PYTHON = python3
TARGET_FILE = manage.py
all: migrations migrate run

migrations:
	$(PYTHON) $(SOURCE_DIR)$(TARGET_FILE) makemigrations

migrate:
	$(PYTHON) $(SOURCE_DIR)$(TARGET_FILE) migrate

run:
	$(PYTHON) $(SOURCE_DIR)$(TARGET_FILE) runserver 0.0.0.0:8000
