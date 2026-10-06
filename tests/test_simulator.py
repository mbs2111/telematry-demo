from telemetry.simulator import TelemetrySimulator


def test_seeded_simulator_generates_valid_readings() -> None:
    first = TelemetrySimulator(seed=17).generate_reading()
    second = TelemetrySimulator(seed=17).generate_reading()

    assert first.speed_kph == second.speed_kph
    assert first.engine_temperature_c == second.engine_temperature_c
    assert 0 <= first.speed_kph <= 130
    assert -90 <= first.gps.latitude <= 90
    assert -180 <= first.gps.longitude <= 180