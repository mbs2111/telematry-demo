# Project Name
Vehicle Telemetry Demo

# Project Description
A small Python demo application that simulates vehicle telemetry. It generates sensor readings (speed, engine temperature, battery voltage, fuel level, GPS position), processes them, and exposes the latest data through a simple API and console output. This is a demo: favor simplicity and readability over completeness.

# Tech Stack
- Python 3.11+
- FastAPI + Uvicorn (REST API)
- Pydantic (data models and validation)
- SQLite via the standard `sqlite3` module (storage)
- pytest (testing)
- Ruff and Black (lint and format)

# Folder Structure
```
telematry_demo/
├── src/
│   └── telemetry/
│       ├── __init__.py
│       ├── models.py        # Pydantic telemetry models
│       ├── simulator.py     # Generates fake vehicle data
│       ├── storage.py       # SQLite persistence
│       └── api.py           # FastAPI app and routes
├── tests/                   # pytest tests mirroring src/
├── requirements.txt
├── copilot-instructions.md
└── README.md
```

# Unit Test Framework
- Use `pytest`; place tests in `tests/` named `test_<module>.py`.
- Test the simulator, models, storage, and API (use FastAPI `TestClient`).
- Use fixtures for shared setup; use an in-memory SQLite DB in tests.
- No real network or hardware access in tests.
- Run with `pytest`.

# Linting Standards
- Follow PEP 8; format with Black (line length 88).
- Lint with Ruff; code must pass with no errors.
- Use type hints on all function signatures.
- Use short docstrings only for public functions and classes.
- Prefer small, single-purpose functions.

# compliance
- Telemetry data in this demo is simulated; do not use real vehicle or driver data.
- Pin dependency versions in `requirements.txt` and use only permissively licensed packages (MIT, BSD, Apache 2.0).
- If real data is introduced later, review applicable privacy regulations (e.g. GDPR) before use.

# Handling Sensitive Data
- Never hardcode secrets, API keys, or credentials; load them from environment variables or a `.env` file excluded via `.gitignore`.
- Treat location (GPS) and vehicle identifiers (VIN) as sensitive: do not log them in plain text; use fake or anonymized values in samples and tests.
- Validate all API input with Pydantic models.
- Do not commit databases or data files containing real telemetry.

# Scoped Instructions
Use the focused instructions in `.github/instructions/` for work in these areas:
- [Python development](./.github/instructions/development.instructions.md) applies to application code under `src/`.
- [Tests](./.github/instructions/testing.instructions.md) applies to pytest files under `tests/`.
- [API routes](./.github/instructions/api.instructions.md) applies to `src/telemetry/api.py`.
- [SQLite persistence](./.github/instructions/storage.instructions.md) applies to `src/telemetry/storage.py`.