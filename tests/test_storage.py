from telemetry.simulator import TelemetrySimulator
from telemetry.storage import TelemetryStorage


def test_storage_round_trips_newest_readings() -> None:
    storage = TelemetryStorage(":memory:")
    first = TelemetrySimulator(seed=1).generate_reading()
    second = TelemetrySimulator(seed=2).generate_reading()

    assert storage.latest() is None
    storage.save(first)
    storage.save(second)

    assert storage.latest() == second
    assert storage.list_readings(limit=1) == [second]
    assert storage.list_readings(limit=2) == [second, first]
    storage.close()