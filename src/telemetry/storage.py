"""SQLite persistence for simulated telemetry readings."""

import sqlite3
from datetime import datetime
from pathlib import Path
from uuid import UUID

from telemetry.models import GPSPosition, TelemetryReading


class TelemetryStorage:
    """Store and retrieve readings using one owned SQLite connection."""

    def __init__(self, database_path: str | Path = "telemetry.db") -> None:
        self._connection = sqlite3.connect(str(database_path), check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS telemetry_readings (
                reading_id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                speed_kph REAL NOT NULL,
                engine_temperature_c REAL NOT NULL,
                battery_voltage REAL NOT NULL,
                fuel_level_percent REAL NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL
            )
            """
        )
        self._connection.commit()

    def save(self, reading: TelemetryReading) -> TelemetryReading:
        """Persist a reading and return it."""
        self._connection.execute(
            """
            INSERT INTO telemetry_readings (
                reading_id, timestamp, speed_kph, engine_temperature_c,
                battery_voltage, fuel_level_percent, latitude, longitude
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(reading.reading_id),
                reading.timestamp.isoformat(),
                reading.speed_kph,
                reading.engine_temperature_c,
                reading.battery_voltage,
                reading.fuel_level_percent,
                reading.gps.latitude,
                reading.gps.longitude,
            ),
        )
        self._connection.commit()
        return reading

    def latest(self) -> TelemetryReading | None:
        """Return the newest reading, if one exists."""
        row = self._connection.execute(
            "SELECT * FROM telemetry_readings ORDER BY timestamp DESC, rowid DESC LIMIT 1"
        ).fetchone()
        return self._from_row(row) if row is not None else None

    def list_readings(self, limit: int = 50) -> list[TelemetryReading]:
        """Return up to ``limit`` readings, newest first."""
        if limit < 1:
            raise ValueError("limit must be at least 1")
        rows = self._connection.execute(
            "SELECT * FROM telemetry_readings ORDER BY timestamp DESC, rowid DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [self._from_row(row) for row in rows]

    def close(self) -> None:
        """Close the owned database connection."""
        self._connection.close()

    @staticmethod
    def _from_row(row: sqlite3.Row) -> TelemetryReading:
        return TelemetryReading(
            reading_id=UUID(row["reading_id"]),
            timestamp=datetime.fromisoformat(row["timestamp"]),
            speed_kph=row["speed_kph"],
            engine_temperature_c=row["engine_temperature_c"],
            battery_voltage=row["battery_voltage"],
            fuel_level_percent=row["fuel_level_percent"],
            gps=GPSPosition(
                latitude=row["latitude"],
                longitude=row["longitude"],
            ),
        )