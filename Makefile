.DEFAULT_GOAL := help

files_for_check ?= src

.PHONY: up
up: ## Create .env file and up all services
	touch .env
	docker-compose up

.PHONY: build
build: ## Build and up containers
	docker-compose up --build

.PHONY: down
uninstall: ## Complete remove containers and named volumes
	docker-compose down --remove-orphans --volumes

.PHONY: init_db
init_db: ## Init database
	docker-compose exec gbh-backend poetry run alembic upgrade head

.PHONY: flake8
flake8:  ## Check code quality
	poetry run flake8

.PHONY: mypy
mypy:  ## Check annotation types
	poetry run mypy ${files_for_check}

.PHONY: help
help: ## Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
