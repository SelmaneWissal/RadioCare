# RadioCare

Plateforme Data Engineering pour le suivi des équipements radio, l'analyse des incidents et la priorisation de la maintenance.

## Milestone 1 — Cadrage et environnement (Semaine 1)

Choix retenu : **données synthétiques** (générateur interne), les données réelles étant indisponibles ou incertaines.

## Structure du dépôt

```
radiocare/
├── README.md
├── docker-compose.yml
├── .env.example
├── .gitignore
├── Makefile
├── config/
├── data/                 (sample/, generated/)
├── scripts/              (generate_data.py, validate_environment.py)
├── src/radiocare/        (ingestion, quality, transformations, database, prioritization, common)
├── airflow/dags/
├── dbt/                  (models/staging, intermediate, marts ; tests/)
├── dashboards/powerbi/
├── tests/                (unit, integration, data_quality, e2e)
├── docs/
│   ├── decisions.md
│   ├── audit_donnees.md
│   ├── kpi.md
│   ├── datamodel_v0.md
│   └── architecture_v1.md
└── .github/workflows/    (ci.yml, cd.yml)
```

## Lancer l'environnement

```bash
make up
```

Puis valider l'environnement :

```bash
python scripts/validate_environment.py
```

## Générer les données synthétiques

```bash
python scripts/generate_data.py
```

Les fichiers générés sont écrits dans `data/generated/` et marqués explicitement comme synthétiques.
