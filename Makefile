.PHONY: setup_venv run_app test_app

setup_venv:
	python3 -m venv venv && . venv/bin/activate \
	&& python3 -m pip install --upgrade pip \
	&& python3 -m pip install -e ".[dev]"

run_app:
	. venv/bin/activate && python3 app/main.py

test_app:
	. venv/bin/activate && pytest -svv
