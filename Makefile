# RadioCare — Makefile
.PHONY: help up down logs validate generate-data test lint

help: ## Affiche l'aide
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

up: ## Démarre l'environnement Docker Compose
	docker compose up -d

down: ## Arrête et supprime les conteneurs
	docker compose down

logs: ## Affiche les logs des conteneurs
	docker compose logs -f

validate: ## Valide l'environnement local
	python scripts/validate_environment.py

generate-data: ## Génère le jeu de données synthétiques
	python scripts/generate_data.py

lint: ## Lint du code Python
	ruff check src scripts tests

test: ## Lance les tests pytest
	pytest
