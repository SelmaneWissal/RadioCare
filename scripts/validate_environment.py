"""Valide que l'environnement RadioCare est correctement configuré."""

from __future__ import annotations

import os
import sys
from pathlib import Path

REQUIRED_ENV = [
    "POSTGRES_USER",
    "POSTGRES_PASSWORD",
    "POSTGRES_DB",
    "POSTGRES_HOST",
    "POSTGRES_PORT",
    "MINIO_ROOT_USER",
    "MINIO_ROOT_PASSWORD",
    "MINIO_PORT",
    "MINIO_BUCKET",
    "AIRFLOW__WEBSERVER__PORT",
]


def load_env(path: str = ".env") -> None:
    """Charge les variables d'un fichier .env s'il existe."""
    env_file = Path(path)
    if not env_file.exists():
        message = (
            f"[INFO] Aucun fichier {path} trouvé, "
            "lecture des variables d'environnement."
        )
        print(message)
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def check_env() -> list[str]:
    missing = [k for k in REQUIRED_ENV if not os.environ.get(k)]
    return missing


def main() -> int:
    load_env()
    missing = check_env()
    if missing:
        print("[ERREUR] Variables d'environnement manquantes :")
        for k in missing:
            print(f"  - {k}")
        print("Copiez .env.example vers .env et renseignez les valeurs.")
        return 1
    print("[OK] Environnement validé : toutes les variables requises sont présentes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
