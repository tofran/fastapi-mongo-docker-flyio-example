help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-21s\033[0m %s\n", $$1, $$2}'


# Host development scripts (docker-compose)

build: ## Build the develpment environment with docker-compose
	docker-compose build

develop: ## Start the development server with docker
	docker-compose run --service-ports -- dev

shell: ## Get a shell inside a new development container
	docker-compose run --service-ports -- dev bash

down: ## Delete docker-compose containers and volumes
	docker-compose down --remove-orphans --volumes

dc-lint: ## Using docker-compose, ensures the code is properlly formatted
	docker-compose run --service-ports -- dev make lint

# General app scripts

start-dev: ## Start a production ready server
	uvicorn app.main:app \
		--host 0.0.0.0 \
		--port 8000 \
		--lifespan=on \
		--use-colors \
		--loop uvloop \
		--http httptools \
		--reload

start-prod: ## Start a production ready server
	uvicorn app.main:app \
		--host 0.0.0.0 \
		--port 8000 \
		--lifespan=on \
		--loop uvloop \
		--http httptools


# Codestyle scripts

lint: ## Ensures the code is properlly formatted
	pycodestyle app
	isort --settings-path=./setup.cfg --check-only app

format:  ## format the code accordig to the configuration
	autopep8 -ir app
	isort --settings-path=./setup.cfg app


# Pipenv scripts - dependency management

lock: ## Refresh pipfile.lock
	pipenv lock

requirements: ## Refresh requirements.txt from pipfile.lock
	pipenv requirements > requirements.txt

requirements_dev: ## Refresh requirements.txt from pipfile.lock
	pipenv requirements --dev > requirements-dev.txt


# Testing scripts

# test: ## Run project tests
# 	docker-compose run --rm web pytest -vv