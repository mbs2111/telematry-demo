import pytest
from fastapi.testclient import TestClient

from telemetry.api import create_app
from telemetry.storage import TelemetryStorage


@pytest.fixture
def client() -> TestClient:
    storage = TelemetryStorage(":memory:")
    with TestClient(create_app(storage)) as test_client:
        yield test_client
    storage.close()


def test_health_and_empty_latest(client: TestClient) -> None:
    assert client.get("/health").json() == {"status": "ok"}

    response = client.get("/telemetry/latest")
    assert response.status_code == 404


def test_generate_and_fetch_readings(client: TestClient) -> None:
    generated = client.post("/telemetry/generate")
    assert generated.status_code == 201
    assert "gps" in generated.json()

    latest = client.get("/telemetry/latest")
    history = client.get("/telemetry", params={"limit": 1})
    assert latest.json() == generated.json()
    assert history.json() == [generated.json()]


def test_history_limit_is_validated(client: TestClient) -> None:
    assert client.get("/telemetry", params={"limit": 0}).status_code == 422