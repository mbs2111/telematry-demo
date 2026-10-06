"""Validated telemetry data models."""

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


class GPSPosition(BaseModel):
    """A simulated GPS position."""

    model_config = ConfigDict(extra="forbid")

    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class TelemetryReading(BaseModel):
    """A single simulated vehicle sensor reading."""

    model_config = ConfigDict(extra="forbid")

    reading_id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    speed_kph: float = Field(ge=0, le=260)
    engine_temperature_c: float = Field(ge=-40, le=200)
    battery_voltage: float = Field(ge=0, le=20)
    fuel_level_percent: float = Field(ge=0, le=100)
    gps: GPSPosition

    @field_validator("timestamp")
    @classmethod
    def timestamp_must_be_timezone_aware(cls, value: datetime) -> datetime:
        """Require timestamps with an explicit timezone."""
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("timestamp must include a timezone")
        return value.astimezone(timezone.utc)