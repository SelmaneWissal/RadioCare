# Milestone 2 — Ingestion et stockage (Semaine 2)

## Objectif
Réaliser une première ingestion de bout en bout.

## Tâches

| ID | Tâche | Resp. | Livrable |
|----|-------|-------|----------|
| M2.1 | Compléter le générateur avec anomalies volontaires (doublons, nulls, dates incohérentes) | A | Script paramétrable et reproductible |
| M2.2 | Développer les lecteurs CSV/JSON et la validation de structure | A | Module `ingestion/` testé |
| M2.3 | Attribuer un `batch_id` et stocker les fichiers bruts dans MinIO | A | Fichiers Bronze et métadonnées du lot |
| M2.4 | Créer les schémas Silver : tables, clés, contraintes, migrations | B | Scripts de migration versionnés |
| M2.5 | Implémenter le chargement idempotent (upsert ou clé de lot) | B, A | Rejeu d'un lot sans doublon |
| M2.6 | Implémenter les premiers contrôles de qualité | C | Module `quality/` |
| M2.7 | Mettre en place la quarantaine et la journalisation (lues, acceptées, rejetées) | C, B | Rejets consultables avec motif |
| M2.8 | Écrire les tests pytest d'ingestion et de validation | A, C | Tests passants |
| M2.9 | Mettre en place le workflow CI : lint, tests unitaires, protection de `main` | B | `ci.yml` actif |

## Critères d'acceptation
Un jeu de données est importé, contrôlé et consultable dans PostgreSQL ; les rejets sont tracés.
