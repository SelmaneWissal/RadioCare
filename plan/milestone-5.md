# Milestone 5 — Extension avancée (Semaine 5, optionnelle)

## Objectif
Intégrer et mesurer une seule extension, choisie selon l'état du projet. Retirée du périmètre dans la variante quatre semaines.

## Options
1. **Kafka** : producteur d'événements simulés (télémétrie), topic Kafka dans Docker Compose, consommateur Python écrivant dans PostgreSQL, mesure de la latence entre émission et traitement.
2. **Détection d'anomalies** : vérifier l'adéquation des données, choisir une méthode (scikit-learn), définir la référence de comparaison, évaluer correctement, documenter méthode, données et limites.
3. **Robustesse et observabilité** : alertes et métriques de pipeline, Grafana technique si utile, règles de qualité supplémentaires, tests de charge.

## Tâches communes

| ID | Tâche | Resp. | Livrable |
|----|-------|-------|----------|
| M5.1 | Choisir l'extension et justifier le choix | Équipe | Décision |
| M5.2 | Développer sur une branche dédiée, sans toucher au socle | Selon option | Code de l'extension |
| M5.3 | Tester et documenter l'extension | A, D | Tests + documentation |
| M5.4 | Vérifier la non-régression du pipeline principal | B, C | Pipeline principal intact |

## Critères d'acceptation
L'extension est fonctionnelle, documentée, mesurée et ne compromet pas le socle. Aucune précision de prédiction n'est annoncée sans évaluation appropriée.
