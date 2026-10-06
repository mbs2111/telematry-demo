"""Deterministic-capable fake telemetry generation."""

import random
from datetime import datetime, timezone

from telemetry.models import GPSPosition, TelemetryReading


class TelemetrySimulator:
    """Generate plausible telemetry without accessing real vehicles."""

    def __init__(self, seed: int | None = None) -> None:
        self._random = random.Random(seed)

    def generate_reading(self) -> TelemetryReading:
        """Generate one simulated sensor reading."""
        return TelemetryReading(
            timestamp=datetime.now(timezone.utc),
            speed_kph=round(self._random.uniform(0, 130), 1),
            engine_temperature_c=round(self._random.uniform(75, 110), 1),
            battery_voltage=round(self._random.uniform(11.8, 14.7), 2),
            fuel_level_percent=round(self._random.uniform(5, 100), 1),
            gps=GPSPosition(
                latitude=round(self._random.uniform(-90, 90), 6),
                longitude=round(self._random.uniform(-180, 180), 6),
            ),
        )