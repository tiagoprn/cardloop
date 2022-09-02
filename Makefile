.PHONY: help
SHELL := /bin/bash
PROJECT_NAME = cardloop

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:  ## Clean python bytecodes, optimized files, logs, cache, coverage...
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -fr .pytest_cache/
	@rm -f coverage.xml
	@rm -f *.log
	@find . -name "celerybeat-schedule*" | xargs rm -rf

requirements: clean  ## setup poetry environment (install project requirements)
	@poetry install

shell: clean  ## activate poetry environment
	@poetry shell

style:	## Run isort and black auto formatting code style in the project
	@echo 'running isort...'
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa .
	@echo 'running black...'
	@black -S -t py39 -l 79 $(PROJECT_NAME)/. --exclude '/(\.git|\.venv|env|build|dist)/'

style-check:  ## Run isort and black check code style
	@echo 'isort check...'
	@isort -v --check -m 3 --trailing-comma --use-parentheses --honor-noqa --color .
	@echo 'black check...'
	@black -S -t py39 -l 79 --check $(PROJECT_NAME)/. --exclude '/(\.git|\.venv|env|build|dist)/'

lint:  ## Run the linter to enforce our coding practices
	@printf '\n --- \n >>> Running linter...<<<\n'
	@pylint --rcfile=.pylintrc $(PROJECT_NAME)/*
	@printf '\n FINISHED! \n --- \n'

test: clean  ## Run the test suite
	@cd $(PROJECT_NAME) && py.test -s -vvv

coverage: clean  ## Run the test coverage report
	@py.test --cov-config .coveragerc --cov $(PROJECT_NAME) $(PROJECT_NAME) --cov-report term-missing

run: ## Run the script on the sample file as input
	@python cardloop/sample_script.py "Hal Jordan"
