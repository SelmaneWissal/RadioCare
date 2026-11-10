# RadioCare — Architecture v1 (M1.9)

## Diagramme (Mermaid)

```mermaid
flowchart LR
    Sources[Sources CSV / JSON<br/>ou données synthétiques]
    Python[Python + Pandas<br/>Ingestion & nettoyage]
    Bronze((Bronze<br/>MinIO<br/>Fichiers bruts par source et date))
    Silver((Silver<br/>PostgreSQL + Python<br/>Nettoyé, dédoublonné, validé))
    Gold((Gold<br/>dbt Core + PostgreSQL<br/>Faits et marts analytiques))
    Restitution[Restitution<br/>Power BI<br/>KPI, priorités, qualité]
    Airflow[Apache Airflow<br/>Orchestration batch 7 étapes<br/>Docker Compose]
    Quarantine[Quarantaine<br/>Enregistrements invalides<br/>avec motif + batch_id]

    Sources --> Python
    Python --> Bronze
    Python --> Quality[Contrôles qualité]
    Quality --> Silver
    Quality -.-> Quarantine
    Silver --> Gold
    Gold --> Restitution
    Airflow --> Python
    Airflow --> dbt[dbt run / dbt test]
```

## Flux de données (7 étapes Airflow, §F5 du CDC)
1. Vérification des entrées.
2. Ingestion des données (lecture CSV/JSON, batch_id, stockage brut MinIO).
3. Contrôles de qualité (quarantaine des enregistrements invalides).
4. Chargement des tables structurées (PostgreSQL Silver).
5. Exécution des modèles dbt (staging → intermediate → marts Gold).
6. Tests des modèles analytiques.
7. Enregistrement du résultat de l'exécution (`pipeline_runs`).

## Stack technologique (§7.1 du CDC)
- Python, Pandas : ingestion et logique métier.
- PostgreSQL : stockage relationnel et analytique.
- MinIO : stockage objet (couche Bronze).
- Apache Airflow : orchestration batch.
- dbt Core : transformations SQL et tests.
- Docker Compose : environnement reproductible.
- Git / GitHub Actions : versionnement et CI/CD.
- pytest : tests unitaires et d'intégration.
- Power BI : visualisation des indicateurs.

## Conteneurs (docker-compose.yml)
- `postgres` : base de données relationnelle (Silver / Gold).
- `minio` : stockage objet (Bronze).
- `airflow` : webserver + scheduler (orchestration).
