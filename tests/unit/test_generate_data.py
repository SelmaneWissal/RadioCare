"""Tests unitaires pour le générateur de données synthétiques RadioCare."""

from __future__ import annotations

import json
import random
from pathlib import Path

from scripts.generate_data import (
    EQUIPMENT_TYPES,
    SEVERITIES,
    SITES,
    STATUSES,
    generate_equipments,
    generate_incidents,
    generate_maintenance,
    generate_sites,
    generate_telemetry,
    inject_anomalies,
)

RNG = random.Random(42)


def test_generate_sites_returns_expected_count() -> None:
    sites = generate_sites(RNG, n=3)
    assert len(sites) == 3
    assert sites[0]["site_id"] == "SITE_01"


def test_generate_equipments_has_required_fields() -> None:
    sites = [{"site_id": s[0], "site_name": s[1]} for s in SITES[:2]]
    equipments = generate_equipments(RNG, sites, n=5)
    assert len(equipments) == 5
    for eq in equipments:
        assert "equipment_id" in eq
        assert "site_id" in eq
        assert "equipment_type" in eq
        assert eq["equipment_type"] in EQUIPMENT_TYPES


def test_generate_incidents_has_required_fields() -> None:
    incidents = generate_incidents(RNG, [{"equipment_id": "EQP_001"}], n=10)
    assert len(incidents) == 10
    for inc in incidents:
        assert "incident_id" in inc
        assert "severity" in inc
        assert inc["severity"] in SEVERITIES
        assert "status" in inc
        assert inc["status"] in STATUSES


def test_generate_maintenance_links_to_incidents() -> None:
    incidents = [
        {"incident_id": "INC_001", "start_time": "2024-01-01 00:00:00"},
        {"incident_id": "INC_002", "start_time": "2024-01-02 00:00:00"},
    ]
    maintenance = generate_maintenance(RNG, incidents, [{"equipment_id": "EQP_001"}])
    assert len(maintenance) == 2
    for m in maintenance:
        assert "maintenance_id" in m
        assert "incident_id" in m
        assert m["incident_id"] in ("INC_001", "INC_002")


def test_generate_telemetry_has_required_fields() -> None:
    telemetry = generate_telemetry(RNG, [{"equipment_id": "EQP_001"}], n=5)
    assert len(telemetry) == 5
    for t in telemetry:
        assert "event_id" in t
        assert "equipment_id" in t
        assert "event_time" in t


def test_inject_anomalies_creates_duplicates() -> None:
    records = [{"id": i, "value": i * 10} for i in range(10)]
    original_count = len(records)
    result = inject_anomalies(RNG, records, rate=0.5)
    assert len(result) > original_count  # des doublons sont ajoutés


def test_inject_anomalies_creates_nulls() -> None:
    records = [{"id": i, "value": i * 10} for i in range(100)]
    result = inject_anomalies(RNG, records, rate=1.0)
    null_count = sum(
        1 for r in result if any(v is None for k, v in r.items() if k != "id")
    )
    assert null_count > 0  # des champs manquants sont injectés


def test_generated_csv_has_header(tmp_path: Path) -> None:
    import scripts.generate_data as gd

    out = tmp_path / "out"
    out.mkdir()
    sites = generate_sites(RNG, n=2)
    gd.write_csv(out / "sites.csv", sites)
    content = (out / "sites.csv").read_text(encoding="utf-8")
    assert "site_id" in content
    assert "site_name" in content


def test_generated_json_is_valid(tmp_path: Path) -> None:
    import scripts.generate_data as gd

    out = tmp_path / "out"
    out.mkdir()
    telemetry = generate_telemetry(RNG, [{"equipment_id": "EQP_001"}], n=3)
    gd.write_json(out / "telemetry.json", telemetry)
    data = json.loads((out / "telemetry.json").read_text(encoding="utf-8"))
    assert len(data) == 3
    assert data[0]["equipment_id"] == "EQP_001"
