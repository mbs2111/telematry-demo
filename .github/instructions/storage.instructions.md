---
name: Telemetry Storage
description: "Use when changing SQLite persistence, schemas, queries, or transaction behavior in the telemetry storage module."
applyTo: "src/telemetry/storage.py"
---

# SQLite Persistence

- Use Python's standard-library `sqlite3` module; keep database operations isolated behind the storage module.
- Parameterize SQL values; never interpolate external input into SQL strings.
- Make connection ownership, transaction boundaries, and cleanup explicit.
- Keep stored telemetry simulated or anonymized; do not commit databases containing real telemetry.
- Test persistence against an in-memory database, including expected behavior for empty or invalid inputs where relevant.