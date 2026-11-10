# RadioCare — Décisions d'architecture (M1.2)

## Décision : données synthétiques

**Décision retenue :** Le projet utilise un **générateur de données synthétiques** comme source de données principale pour le Milestone 1 et le socle initial.

### Justification
- La disponibilité des données réelles est inconnue au démarrage (risque majeur identifié, §5 du CDC).
- Un générateur permet de disposer immédiatement de données cohérentes, avec des anomalies volontaires (doublons, champs manquants, dates incohérentes) pour tester les contrôles de qualité.
- Cela débloque l'ingestion et les tests dès la semaine 1 sans attendre l'accès aux données réelles.

### Traçabilité
- Les données générées sont explicitement identifiées comme synthétiques (`synthetic: true` dans `data/generated/_meta.json` et en-tête des fichiers).
- Les résultats obtenus sur données simulées ne sont jamais présentés comme des performances validées en production (§5.2 du CDC).
- Si des données réelles deviennent accessibles, la décision sera réévaluée et ce document mis à jour.

### Fichiers associés
- `scripts/generate_data.py` : générateur paramétrable et reproductible (graine fixe).
- `data/generated/` : jeu de données d'exemple généré.

### Référents
- Responsable : A (ingestion, génération de données)
- Validation : Équipe
