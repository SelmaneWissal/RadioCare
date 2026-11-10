# Milestone 1 — Cadrage et environnement (Semaine 1)

## Objectif
Architecture et environnement validés.

## Tâches

| ID | Tâche | Resp. | Livrable |
|----|-------|-------|----------|
| M1.1 | Auditer les données accessibles (formats, période, volume, champs, clés, confidentialité) | A, C | Note d'audit des données |
| M1.2 | Décider entre données réelles et synthétiques | Équipe | Décision dans `docs/decisions.md` |
| M1.3 | Définir les besoins métier, les KPI et leurs hypothèses de calcul | C, D | Fiche des KPI |
| M1.4 | Définir le modèle de données initial et le dictionnaire v0 | B, C | Schéma et dictionnaire |
| M1.5 | Initialiser Git/GitHub : branches, règles de PR, Kanban, conventions | B | Dépôt structuré |
| M1.6 | Écrire le Docker Compose minimal : PostgreSQL, MinIO, Airflow | B | `docker-compose.yml` |
| M1.7 | Écrire `.env.example`, `Makefile`, `validate_environment.py` | B, A | Environnement vérifiable en une commande |
| M1.8 | Produire un jeu d'exemple ou la première version du générateur | A | Fichiers marqués synthétiques |
| M1.9 | Dessiner le diagramme d'architecture v1 | D | Diagramme dans `docs/` |

## Choix retenu
Données **synthétiques** (générateur interne), les données réelles étant indisponibles ou incertaines.

## Critères d'acceptation
Tous les membres lancent l'environnement local et expliquent le modèle initial.
