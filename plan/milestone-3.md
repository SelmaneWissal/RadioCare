# Milestone 3 — Transformation et orchestration (Semaine 3)

## Objectif
Obtenir un pipeline batch automatisé.

## Tâches

| ID | Tâche | Resp. | Livrable |
|----|-------|-------|----------|
| M3.1 | Développer le nettoyage Silver : normalisation, déduplication, valeurs manquantes | C | Règles documentées dans `docs/` |
| M3.2 | Créer le projet dbt : sources, modèles staging et intermediate | C | `dbt run` réussi |
| M3.3 | Écrire les tests dbt : not_null, unique, relationships, valeurs acceptées | C | `dbt test` réussi |
| M3.4 | Créer le DAG Airflow en sept étapes | B | DAG visible et exécutable |
| M3.5 | Créer la table `pipeline_runs` : statut, durées, volumes | B | Historique des exécutions |
| M3.6 | Gérer les échecs : retries, journalisation, reprise d'une tâche | B | Échec simulé puis reprise sans corruption |
| M3.7 | Tester la réexécution : rejeu d'un lot sans doublon | A, B | Test d'intégration automatisé |
| M3.8 | Tester le parcours fichier, MinIO, PostgreSQL, dbt | A, C | Test d'intégration vert |
| M3.9 | Tenir la revue de périmètre : go / no-go sur l'extension | Équipe | Décision consignée |
| M3.10 | Étendre la CI : tests dbt sur PostgreSQL jetable, build Docker Compose, intégration | B, C | Pipeline CI complet |

## Critères d'acceptation
Le pipeline fonctionne de manière reproductible ; les erreurs sont détectées et les reprises démontrées.
