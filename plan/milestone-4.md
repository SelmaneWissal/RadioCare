# Milestone 4 — Analytics et première livraison (Semaine 4)

## Objectif
Livrer une version minimale complète et démontrable.

## Tâches

| ID | Tâche | Resp. | Livrable |
|----|-------|-------|----------|
| M4.1 | Construire les modèles Gold : `fact_incidents`, `fact_maintenance`, `mart_equipment_health` | C | Tables disponibles et testées |
| M4.2 | Construire `fact_availability` si les données le permettent, sinon documenter la limite | C | Modèle ou note de limite |
| M4.3 | Calculer les KPI avec hypothèses documentées | C | KPI vérifiables par requête SQL |
| M4.4 | Définir et implémenter le score de priorisation explicable | D, C | Module `prioritization/` |
| M4.5 | Écrire les tests unitaires du score (cas limites, valeurs manquantes) | D | Tests passants |
| M4.6 | Construire le dashboard Power BI | D | Fichier `.pbix` dans `dashboards/powerbi/` |
| M4.7 | Connecter Power BI à la couche Gold et vérifier les chiffres | D, C | Chiffres du dashboard égaux aux résultats SQL |
| M4.8 | Exécuter le premier test de bout en bout | D | Scénario e2e exécuté |
| M4.9 | Mettre à jour le dictionnaire (v1) et le diagramme | C, D | Documents à jour |

## Critères d'acceptation
Les données sources traversent le pipeline jusqu'au dashboard et les résultats sont vérifiables.
