---
name: Telemetry API
description: "Use when changing FastAPI routes or request and response behavior in the telemetry API."
applyTo: "src/telemetry/api.py"
---

# Telemetry API

- Keep route handlers thin; delegate persistence and domain behavior to their owning modules.
- Validate request data with the existing Pydantic models and return explicit, consistent HTTP responses.
- Do not expose secrets, raw database details, or sensitive GPS and vehicle identifiers in logs or error responses.
- Cover route behavior with FastAPI `TestClient` tests, including invalid input and relevant failure cases.
- Do not make real network or hardware calls from route tests.