import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from app import app  # noqa: E402


def test_home_endpoint_returns_expected_payload():
    client = app.test_client()

    response = client.get("/")
    payload = response.get_json()

    assert response.status_code == 200
    assert response.is_json
    assert payload["message"] == "Azure Application Platform Lab"
    assert payload["status"] == "running"
    assert payload["docs"] == "/health"


def test_health_endpoint_reports_healthy_service():
    client = app.test_client()

    response = client.get("/health")
    payload = response.get_json()

    assert response.status_code == 200
    assert response.is_json
    assert payload == {
        "service": "azure-app-platform-lab",
        "status": "healthy",
        "version": "1.0.0",
    }


def test_info_endpoint_exposes_non_sensitive_runtime_metadata():
    client = app.test_client()

    response = client.get("/info")
    payload = response.get_json()

    assert response.status_code == 200
    assert response.is_json
    assert payload["app"] == "Azure Application Platform Lab"
    assert payload["version"] == "1.0.0"
    assert payload["python_port"] == 8000
    assert "description" in payload
    assert "password" not in payload
    assert "token" not in payload
