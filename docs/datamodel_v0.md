# RadioCare — Modèle de données v0 (M1.4)

Schéma initial et dictionnaire de données. Adapté aux colonnes réellement disponibles ; les champs facultatifs ne sont pas inventés.

## Tables sources (Bronze / Silver)

### sites
| Attribut | Type | Clé | Description |
|----------|------|-----|-------------|
| site_id | texte | PK | Identifiant du site |
| site_name | texte | | Nom du site |
| region | texte | | Région géographique |
| site_category | texte | | Catégorie du site |
| criticality | texte | | Criticité du site (Toujours disponible) |

### equipment
| Attribut | Type | Clé | Description |
|----------|------|-----|-------------|
| equipment_id | texte | PK | Identifiant de l'équipement |
| site_id | texte | FK → sites.site_id | Site d'appartenance |
| equipment_type | texte | | Type d'équipement |
| manufacturer | texte | | Fabricant |
| installation_date | date | | Date d'installation |
| criticality | texte | | Criticité de l'équipement |

### incidents
| Attribut | Type | Clé | Description |
|----------|------|-----|-------------|
| incident_id | texte | PK | Identifiant de l'incident |
| equipment_id | texte | FK → equipment.equipment_id | Équipement concerné |
| incident_type | texte | | Type d'incident |
| severity | texte | | Gravité (valeurs autorisées contrôlées) |
| start_time | datetime | | Début de l'incident |
| end_time | datetime | | Fin de l'incident (si clos) |
| known_cause | texte | | Cause connue |
| status | texte | | Statut (Ouvert, En cours, Cloturé, En attente) |

### maintenance
| Attribut | Type | Clé | Description |
|----------|------|-----|-------------|
| maintenance_id | texte | PK | Identifiant de l'intervention |
| incident_id | texte | FK → incidents.incident_id | Incident traité |
| equipment_id | texte | FK → equipment.equipment_id | Équipement |
| intervention_time | datetime | | Heure d'intervention |
| duration | entier | | Durée (heures) |
| result | texte | | Résultat de la maintenance |
| cost | numérique | ? | Coût (facultatif) |

### telemetry
| Attribut | Type | Clé | Description |
|----------|------|-----|-------------|
| event_id | texte | PK | Identifiant de l'événement |
| equipment_id | texte | FK → equipment.equipment_id | Équipement mesuré |
| event_time | datetime | | Horodatage de la mesure |
| signal_level | numérique | ? | Niveau de signal |
| temperature | numérique | ? | Température |
| error_rate | numérique | ? | Taux d'erreur |
| availability_status | texte | ? | Statut de disponibilité |

## Tables analytiques (Gold)

### fact_incidents
Fait d'incidents pour l'analyse (issue de `incidents` nettoyés).

### fact_maintenance
Fait d'interventions de maintenance (issue de `maintenance` nettoyés).

### fact_availability
Disponibilité, si les données le permettent (issue de `telemetry`).

### mart_equipment_health
Synthèse par équipement et score de priorisation.

## Règles de qualité associées
- Présence des identifiants obligatoires (PK, FK).
- Validité des dates.
- Cohérence des valeurs numériques (plages documentées).
- Unicité des identifiants appropriés.
- Existence des équipements référencés par les incidents.
- Cohérence des relations entre les tables.
- Présence de valeurs autorisées pour les catégories et niveaux de gravité.
