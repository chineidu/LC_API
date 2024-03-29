.PHONY: help setup_venv run_app run_lint run_style run_test run_checks

help:
	@echo "Commands:"
	@echo "\tsetup_venv:       creates a virtual environment."
	@echo "\trun_app:          runs the app."
	@echo "\trun_lint:         runs the linting."
	@echo "\trun_style:        runs style and type formatting."
	@echo "\trun_checks:       runs tests and code quality (RECOMMENDEED)."
	@echo

setup_venv:
	python3 -m venv venv && . venv/bin/activate \
	&& python3 -m pip install --upgrade pip \
	&& python3 -m pip install -e ".[dev]"

run_app:
	. venv/bin/activate && python3 app/main.py

run_test:
	. venv/bin/activate && pytest -svv

run_lint:
	. venv/bin/activate && black app && isort app

run_style:
	. venv/bin/activate && pylint --recursive=y app && mypy app


run_checks: run_test run_lint run_style
