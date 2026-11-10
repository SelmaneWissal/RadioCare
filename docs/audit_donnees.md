# RadioCare — Note d'audit des données (M1.1)

## Contexte
Première action obligatoire (semaine 1, §5.1 du CDC) : déterminer les données accessibles, leurs formats, leur période historique, leur volume approximatif, les champs disponibles, les clés reliant équipements/incidents/interventions, et les éventuelles restrictions de confidentialité.

## Constat
- Aucune donnée réelle n'est disponible à ce stade dans le dépôt.
- La disponibilité des données réelles est inconnue (risque majeur).

## Décision
Utiliser un **générateur de données synthétiques** (voir `docs/decisions.md`).

## Données synthétiques générées

| Fichier | Format | Lignes (exemple) | Champs clés |
|---------|--------|------------------|-------------|
| `sites.csv` | CSV | 5 | site_id, site_name, region, site_category, criticality |
| `equipments.csv` | CSV | 30 | equipment_id, site_id, equipment_type, manufacturer, installation_date, criticality |
| `incidents.csv` | CSV | 60 | incident_id, equipment_id, incident_type, severity, start_time, end_time, known_cause, status |
| `maintenance.csv` | CSV | 40 | maintenance_id, incident_id, equipment_id, intervention_time, duration, result, cost |
| `telemetry.json` | JSON | 200 | event_id, equipment_id, event_time, signal_level, temperature, error_rate, availability_status |

## Clés reliant les tables
- `sites.site_id` → `equipments.site_id`
- `equipments.equipment_id` → `incidents.equipment_id`, `maintenance.equipment_id`, `telemetry.equipment_id`
- `incidents.incident_id` → `maintenance.incident_id`

## Anomalies volontaires injectées
- Champs manquants sur des attributs non critiques (~8% des enregistrements).
- Doublons (~4% des enregistrements).
- Dates incohérentes possibles.

## Confidentialité
Aucune donnée personnelle ou confidentielle n'est présente (données synthétiques).
