"""FastAPI endpoints for simulated telemetry."""

import os
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI, HTTPException, Query

from telemetry.models import TelemetryReading
from telemetry.simulator import TelemetrySimulator
from telemetry.storage import TelemetryStorage


def create_app(storage: TelemetryStorage | None = None) -> FastAPI:
    """Create the API app with optional injected storage for tests."""
    owns_storage = storage is None
    telemetry_storage = storage
    simulator = TelemetrySimulator()

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        nonlocal telemetry_storage
        if owns_storage:
            telemetry_storage = TelemetryStorage(
                os.getenv("TELEMETRY_DB_PATH", "telemetry.db")
            )
        try:
            yield
        finally:
            if owns_storage and telemetry_storage is not None:
                telemetry_storage.close()
                telemetry_storage = None

    def get_storage() -> TelemetryStorage:
        if telemetry_storage is None:
            raise RuntimeError("Telemetry storage is not initialized")
        return telemetry_storage

    app = FastAPI(title="Vehicle Telemetry Demo", lifespan=lifespan)

    @app.get("/health")
    def health() -> dict[str, str]:
        """Report that the API process is ready."""
        return {"status": "ok"}

    @app.post("/telemetry/generate", response_model=TelemetryReading, status_code=201)
    def generate_reading() -> TelemetryReading:
        """Generate and persist a fake telemetry reading."""
        return get_storage().save(simulator.generate_reading())

    @app.get("/telemetry/latest", response_model=TelemetryReading)
    def latest_reading() -> TelemetryReading:
        """Return the latest reading or a 404 when none exists."""
        reading = get_storage().latest()
        if reading is None:
            raise HTTPException(status_code=404, detail="No telemetry readings available")
        return reading

    @app.get("/telemetry", response_model=list[TelemetryReading])
    def readings(
        limit: int = Query(default=50, ge=1, le=500),
    ) -> list[TelemetryReading]:
        """Return recent readings, newest first."""
        return get_storage().list_readings(limit)

    return app


app = create_app()