# RadioCare — Fiche des KPI (M1.3)

Besoins métier, indicateurs et hypothèses de calcul. À confirmer et figer lors de la tâche M1.3. Un indicateur n'est calculé que si les champs nécessaires existent.

| Indicateur | Définition proposée | Données nécessaires | Disponible synthétique |
|------------|---------------------|---------------------|------------------------|
| Nombre d'incidents | Comptage par période, type, gravité, équipement, site | `incidents` | Oui |
| Durée d'indisponibilité | `end_time − start_time` par incident, cumulée par équipement | `incidents.start_time`, `incidents.end_time` | Oui (si clos) |
| Durée moyenne de résolution | Moyenne de la durée des incidents clos | `start_time`, `end_time`, `status` | Oui |
| Récurrence | Nombre d'incidents d'un équipement sur une fenêtre récente | `incidents`, `equipment_id` | Oui |
| Interventions par résultat | Répartition des résultats de maintenance | `maintenance.result` | Oui |
| Disponibilité | Part du temps en service (télémétrie ou périodes d'indisponibilité fiables) | `telemetry`, `availability_status` | Oui |

## Hypothèses de calcul
- Un incident est "clos" si `status = 'Cloturé'` et `end_time` renseigné.
- La durée d'indisponibilité est exprimée en heures.
- La fenêtre de récurrence est à définir (M4.4).
- La disponibilité est calculée uniquement si `telemetry.availability_status` est renseigné.

## Responsables
- C, D
