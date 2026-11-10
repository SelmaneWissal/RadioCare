"""Générateur de données synthétiques pour RadioCare.

Produit des fichiers CSV/JSON cohérents (équipements, sites, incidents,
interventions, télémétrie) avec des anomalies volontaires (doublons, nulls,
dates incohérentes) pour tester les contrôles de qualité.

Les fichiers générés sont explicitement marqués comme synthétiques.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

SITES = [
    ("SITE_01", "Site Nord", "Nord", "Haute tension", "Critique"),
    ("SITE_02", "Site Sud", "Sud", "Moyenne tension", "Important"),
    ("SITE_03", "Site Est", "Est", "Haute tension", "Critique"),
    ("SITE_04", "Site Ouest", "Ouest", "Moyenne tension", "Standard"),
    ("SITE_05", "Site Centre", "Centre", "Moyenne tension", "Important"),
]

EQUIPMENT_TYPES = ["Relais", "Antenne", "Routeur", "Amplificateur", "Switch"]
MANUFACTURERS = ["NetBuild", "RadioTech", "WaveLink", "TelecomPlus"]
INCIDENT_TYPES = ["Coupure", "Dégradation", "Interférence", "Matériel"]
SEVERITIES = ["Faible", "Moyenne", "Élevée", "Critique"]
STATUSES = ["Ouvert", "En cours", "Cloturé", "En attente"]
MAINTENANCE_RESULTS = ["Réparé", "En attente de pièce", "Non résolu", "Escaladé"]

RNG_SEED = 42


def _rand_date(start: datetime, end: datetime, rng: random.Random) -> datetime:
    return start + timedelta(seconds=rng.randint(0, int((end - start).total_seconds())))


def generate_sites(rng: random.Random, n: int = len(SITES)) -> list[dict]:
    return [
        {
            "site_id": s[0],
            "site_name": s[1],
            "region": s[2],
            "site_category": s[3],
            "criticality": s[4],
        }
        for s in SITES[:n]
    ]


def generate_equipments(rng: random.Random, sites: list[dict], n: int = 30) -> list[dict]:
    site_ids = [s["site_id"] for s in sites]
    equipments = []
    for i in range(1, n + 1):
        eid = f"EQP_{i:03d}"
        install = _rand_date(datetime(2018, 1, 1), datetime(2023, 12, 31), rng)
        equipments.append(
            {
                "equipment_id": eid,
                "site_id": rng.choice(site_ids),
                "equipment_type": rng.choice(EQUIPMENT_TYPES),
                "manufacturer": rng.choice(MANUFACTURERS),
                "installation_date": install.strftime("%Y-%m-%d"),
                "criticality": rng.choice(["Critique", "Important", "Standard"]),
            }
        )
    return equipments


def generate_incidents(
    rng: random.Random, equipments: list[dict], n: int = 60
) -> list[dict]:
    eq_ids = [e["equipment_id"] for e in equipments]
    incidents = []
    for i in range(1, n + 1):
        iid = f"INC_{i:03d}"
        start = _rand_date(datetime(2024, 1, 1), datetime(2024, 12, 31), rng)
        severity = rng.choice(SEVERITIES)
        status = rng.choice(STATUSES)
        end = None
        if status == "Cloturé":
            end = (start + timedelta(hours=rng.randint(1, 72))).strftime("%Y-%m-%d %H:%M:%S")
        incidents.append(
            {
                "incident_id": iid,
                "equipment_id": rng.choice(eq_ids),
                "incident_type": rng.choice(INCIDENT_TYPES),
                "severity": severity,
                "start_time": start.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": end,
                "known_cause": rng.choice(["Oui", "Non", ""]),
                "status": status,
            }
        )
    return incidents


def generate_maintenance(rng: random.Random, incidents: list[dict], equipments: list[dict]) -> list[dict]:
    eq_ids = [e["equipment_id"] for e in equipments]
    maintenance = []
    for i, inc in enumerate(incidents[:40], start=1):
        mid = f"MAINT_{i:03d}"
        maintenance.append(
            {
                "maintenance_id": mid,
                "incident_id": inc["incident_id"],
                "equipment_id": rng.choice(eq_ids),
                "intervention_time": inc["start_time"],
                "duration": rng.randint(1, 24),
                "result": rng.choice(MAINTENANCE_RESULTS),
                "cost": round(rng.uniform(50, 5000), 2),
            }
        )
    return maintenance


def generate_telemetry(rng: random.Random, equipments: list[dict], n: int = 200) -> list[dict]:
    eq_ids = [e["equipment_id"] for e in equipments]
    telemetry = []
    for i in range(1, n + 1):
        event_time = _rand_date(datetime(2024, 1, 1), datetime(2024, 12, 31), rng)
        telemetry.append(
            {
                "event_id": f"TEL_{i:05d}",
                "equipment_id": rng.choice(eq_ids),
                "event_time": event_time.strftime("%Y-%m-%d %H:%M:%S"),
                "signal_level": round(rng.uniform(-100, -40), 1),
                "temperature": round(rng.uniform(-10, 50), 1),
                "error_rate": round(rng.uniform(0, 10), 2),
                "availability_status": rng.choice(["Disponible", "Indisponible", "Degradé"]),
            }
        )
    return telemetry


def inject_anomalies(rng: random.Random, records: list[dict], rate: float = 0.08) -> list[dict]:
    """Injecte des anomalies : doublons, champs manquants, dates incohérentes."""
    for rec in records:
        if rng.random() < rate:
            # Champ manquant sur un attribut non critique
            keys = [k for k in rec.keys() if k not in ("equipment_id", "incident_id", "event_id")]
            if keys:
                rec[rng.choice(keys)] = None
    # Doublons (quelques enregistrements répétés)
    dup_count = max(1, int(len(records) * rate * 0.5))
    for _ in range(dup_count):
        records.append(dict(rng.choice(records)))
    return records


def write_csv(path: Path, records: list[dict]) -> None:
    import csv

    if not records:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)


def write_json(path: Path, records: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(description="Générateur de données synthétiques RadioCare")
    parser.add_argument("--output", default="data/generated", help="Répertoire de sortie")
    parser.add_argument("--seed", type=int, default=RNG_SEED, help="Graine aléatoire")
    parser.add_argument("--equipments", type=int, default=30, help="Nombre d'équipements")
    parser.add_argument("--incidents", type=int, default=60, help="Nombre d'incidents")
    parser.add_argument("--telemetry", type=int, default=200, help="Nombre de mesures télémétrie")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    sites = generate_sites(rng, args.equipments // 3 or 1)
    equipments = generate_equipments(rng, sites, args.equipments)
    incidents = generate_incidents(rng, equipments, args.incidents)
    maintenance = generate_maintenance(rng, incidents, equipments)
    telemetry = generate_telemetry(rng, equipments, args.telemetry)

    # Marquage explicite : données synthétiques
    meta = {
        "synthetic": True,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "seed": args.seed,
        "description": "Données synthétiques générées pour le développement de RadioCare. Ne pas présenter comme des données réelles.",
    }
    (out / "_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    write_csv(out / "sites.csv", sites)
    write_csv(out / "equipments.csv", equipments)
    write_csv(out / "incidents.csv", inject_anomalies(rng, incidents))
    write_csv(out / "maintenance.csv", maintenance)
    write_json(out / "telemetry.json", telemetry)

    print(f"[OK] Données synthétiques générées dans {out}/")
    print(f"  - {len(sites)} sites")
    print(f"  - {len(equipments)} équipements")
    print(f"  - {len(incidents)} incidents")
    print(f"  - {len(maintenance)} interventions maintenance")
    print(f"  - {len(telemetry)} mesures télémétrie")
    print("[NOTE] Marques 'synthetic: true' dans _meta.json et en-tête des fichiers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
