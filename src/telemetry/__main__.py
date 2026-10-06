"""Console entry point for a one-reading simulator preview."""

import json

from telemetry.simulator import TelemetrySimulator


def main() -> None:
    """Print one simulated reading without GPS coordinates."""
    reading = TelemetrySimulator().generate_reading()
    print(json.dumps(reading.model_dump(mode="json", exclude={"gps"}), indent=2))


if __name__ == "__main__":
    main()