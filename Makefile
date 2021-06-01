# Makefile

SHELL := /usr/local/bin/bash
venv := $(shell basename "$$VIRTUAL_ENV")

.PHONY: init
init:
	@echo -n "virtual environment '$(venv)' ... "
	@[ -z $$VIRTUAL_ENV ] && echo please check && exit 1 || echo ok
	@pip install -r requirements.txt
	@pip install pytest
	@pip install twine
	@pip install travis
	@pip install build


.PHONY: install
install:
	@python setup.py install

.PHONY: test
test:
	@pytest -v

.PHONY: build
build:
	@python -m build --sdist
	@python -m build --wheel

.PHONY: test_upload
test_upload:
	@echo test
	@twine upload --repository testpypi dist/*

.PHONY: upload
upload:
	@echo NOT YET AVAILABLE

.PHONY: clean
clean:
	@find . -type f -iname '*.pyc' -delete
	@find . -type d -iname __pycache__ -delete
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/