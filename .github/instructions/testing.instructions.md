---
name: Python Tests
description: "Use when writing or changing pytest tests; covers fixtures, API testing, SQLite isolation, and deterministic telemetry tests."
applyTo: "tests/**/*.py"
---

# Python Tests

- Use pytest and name test files `test_<module>.py` to mirror the `src/` modules.
- Keep tests deterministic; do not access real networks, hardware, vehicle data, or external services.
- Use fixtures for shared setup and an in-memory SQLite database for persistence tests.
- Test validation failures and relevant edge cases as well as successful behavior.
- Exercise FastAPI routes with `TestClient`; do not start a live server in tests.
- Use fake or anonymized telemetry values, and avoid logging GPS coordinates or vehicle identifiers.
- Run the suite with `pytest`.