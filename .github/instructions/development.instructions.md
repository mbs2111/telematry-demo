---
name: Python Development
description: "Use when creating or changing application code in src; covers Python style, typing, dependencies, and telemetry demo constraints."
applyTo: "src/**/*.py"
---

# Python Development

- Keep the demo small, readable, and deterministic; prefer single-purpose functions.
- Add type hints to every function signature and short docstrings to public functions and classes.
- Follow PEP 8, format with Black at 88 columns, and keep code Ruff-clean.
- Use the existing Python 3.11+, FastAPI, Pydantic, and standard-library SQLite stack. Pin any new dependency and use only permissively licensed packages.
- Generate simulated telemetry only. Use fake or anonymized values, and never log GPS coordinates or vehicle identifiers in plain text.
- Validate external input with Pydantic models and keep secrets out of source code.