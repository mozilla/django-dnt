export DJANGO_SETTINGS_MODULE = testapp.settings
export PYTHONPATH := $(shell pwd)

clean:
	git clean -Xfd

develop:
	pip install -r requirements.dev.txt

lint:
	flake8 .

test:
	django-admin test

coverage: clean
	coverage erase
	coverage run --branch --source=dnt `which django-admin` test

coveragehtml: coverage
	coverage html
	python -m webbrowser file://$(CURDIR)/htmlcov/index.html

qa: lint coveragehtml

.PHONY: clean test qa
