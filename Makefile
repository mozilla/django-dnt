export DJANGO_SETTINGS_MODULE = testapp.settings
export PYTHONPATH := $(shell pwd)
.PHONY: help clean coverage coveragehtml develop lint qa qa-all release sdist test test-all

help:
	@echo "clean - remove all artifacts"
	@echo "coverage - check code coverage"
	@echo "coveragehtml - display code coverage in browser"
	@echo "develop - install development requirements"
	@echo "lint - check style with flake8"
	@echo "qa - run linters and test coverage"
	@echo "qa-all - run QA plus tox and packaging"
	@echo "release - package and upload a release"
	@echo "sdist - package"
	@echo "test - run tests"
	@echo "test-all - run tests on every Python version with tox"
	@echo "test-release - upload a release to the test PyPI server"

clean:
	git clean -Xfd

develop:
	pip install -r requirements.dev.txt

lint:
	flake8 .

test:
	django-admin test

test-all:
	tox --skip_missing_interpreters

coverage: clean
	coverage erase
	coverage run --branch --source=dnt `which django-admin` test

coveragehtml: coverage
	coverage html
	python -m webbrowser file://$(CURDIR)/htmlcov/index.html

qa: lint coveragehtml

qa-all: qa sdist test-all

sdist:
	python setup.py sdist bdist_wheel
	ls -l dist
	check-manifest
	pyroma dist/`ls -t dist | grep tar.gz | head -n1`

release: clean sdist
	twine upload dist/*
	python -m webbrowser -n https://pypi.python.org/pypi/django-dnt

# Add [test] section to ~/.pypirc, https://testpypi.python.org/pypi
test-release: clean sdist
	twine upload --repository test dist/*
	python -m webbrowser -n https://testpypi.python.org/pypi/django-dnt
