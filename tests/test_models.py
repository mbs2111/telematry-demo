from datetime import datetime

import pytest
from pydantic import ValidationError

from telemetry.models import GPSPosition, TelemetryReading


def test_reading_requires_timezone_aware_timestamp() -> None:
    with pytest.raises(ValidationError, match="timestamp must include a timezone"):
        TelemetryReading(
            timestamp=datetime(2025, 1, 1),
            speed_kph=0,
            engine_temperature_c=90,
            battery_voltage=12.5,
            fuel_level_percent=50,
            gps=GPSPosition(latitude=0, longitude=0),
        )


def test_gps_rejects_out_of_range_coordinates() -> None:
    with pytest.raises(ValidationError):
        GPSPosition(latitude=91, longitude=0)