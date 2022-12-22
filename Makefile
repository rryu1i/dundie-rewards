.PHONY: install virtualenv ipython clean pflake8


install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[test,dev]'


vritualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython


test:
	@.venv/bin/pytest -vv -s tests/


testci:
	@pytest -v --junitxml=test-result.xml


watch:
	# @.venv/bin/ptw -- -vv -s tests/
	@ls **/*.py | entr pytest


clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build


lint:  # analise estatica
	@.venv/bin/pflake8
