"""Tests d'intégration : disponibilité des services CI (Postgres, MinIO)."""

from __future__ import annotations

import os
import socket
import urllib.request


def test_postgres_is_reachable() -> None:
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = int(os.getenv("POSTGRES_PORT", "5432"))
    with socket.create_connection((host, port), timeout=5):
        pass


def test_minio_health_endpoint_returns_200() -> None:
    host = os.getenv("MINIO_HOST", "localhost")
    port = int(os.getenv("MINIO_PORT", "9000"))
    url = f"http://{host}:{port}/minio/health/live"
    with urllib.request.urlopen(url, timeout=5) as response:
        assert response.status == 200
