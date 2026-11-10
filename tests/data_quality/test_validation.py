"""Tests de qualité des données pour RadioCare."""

from __future__ import annotations

import random

from scripts.generate_data import (
    generate_incidents,
    generate_equipments,
    inject_anomalies,
    SITES,
)

RNG = random.Random(42)


def test_incident_severity_values_are_authorized() -> None:
    """Toutes les sévérités d'incident doivent figurer dans la liste autorisée."""
    incidents = generate_incidents(RNG, [{"equipment_id": "EQP_001"}], n=50)
    authorized = {"Faible", "Moyenne", "Élevée", "Critique"}
    for inc in incidents:
        assert (
            inc["severity"] in authorized
        ), f"Sévérité non autorisée: {inc['severity']}"


def test_incident_status_values_are_authorized() -> None:
    """Tous les statuts d'incident doivent figurer dans la liste autorisée."""
    incidents = generate_incidents(RNG, [{"equipment_id": "EQP_001"}], n=50)
    authorized = {"Ouvert", "En cours", "Cloturé", "En attente"}
    for inc in incidents:
        assert inc["status"] in authorized, f"Statut non autorisé: {inc['status']}"


def test_incident_end_time_only_when_closed() -> None:
    """Un incident non cloturé ne doit pas avoir d'end_time."""
    incidents = generate_incidents(RNG, [{"equipment_id": "EQP_001"}], n=50)
    for inc in incidents:
        if inc["status"] != "Cloturé":
            assert (
                inc["end_time"] is None
            ), f"Incident {inc['incident_id']} non cloturé mais end_time renseigné"


def test_equipment_site_id_references_existing_site() -> None:
    """Chaque équipement doit référencer un site existant."""
    site_ids = {s[0] for s in SITES}
    sites = [{"site_id": s[0], "site_name": s[1]} for s in SITES]
    equipments = generate_equipments(RNG, sites, n=30)
    for eq in equipments:
        assert eq["site_id"] in site_ids, f"Site {eq['site_id']} inexistant"


def test_injected_anomalies_are_detectable() -> None:
    """Les anomalies injectées (nulls, doublons) doivent être détectables."""
    records = [{"id": i, "value": i} for i in range(20)]
    result = inject_anomalies(RNG, records, rate=0.5)
    has_null = any(any(v is None for v in r.values()) for r in result)
    has_duplicate = len(result) != len({r["id"] for r in result})
    assert has_null or has_duplicate, "Aucune anomalie injectée détectée"
