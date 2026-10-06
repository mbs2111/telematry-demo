---
name: Generate Unit Tests
description: Create or update focused pytest unit tests for a telemetry module or behavior.
argument-hint: Name the module or behavior to test, plus any expected behavior or edge cases.
agent: agent
---
Create or update unit tests for: **${input:target:Which module or behavior should be tested?}**

Follow these steps:

1. Read the implementation under `src/telemetry/`, existing related tests under `tests/`, and applicable guidance in [testing.instructions.md](../instructions/testing.instructions.md). Also follow [copilot-instructions.md](../../copilot-instructions.md).
2. Add or update the matching `tests/test_<module>.py`. Keep changes scoped to tests unless the request explicitly asks for implementation changes.
3. Use pytest, descriptive test names, type hints, fixtures when setup is shared, and deterministic fake inputs. Cover normal behavior plus meaningful validation, empty-state, boundary, and failure cases relevant to the target.
4. Use an in-memory SQLite database for storage/API tests, and FastAPI `TestClient` for route tests. Never use real network, hardware, vehicle, or driver data.
5. GPS coordinates and vehicle identifiers are sensitive: use only fake values and avoid printing or logging them. Do not add secrets or external-service dependencies.
6. Run the narrowest relevant test file first. If it passes, report the command and result; if it fails, diagnose and fix test issues without changing unrelated code. Run the full suite when the change may affect shared behavior.

Keep tests simple and consistent with the existing project style. Summarize the cases added and any validation that could not be run.
