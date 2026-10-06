# Vehicle Telemetry Demo

A small Python application that generates fake vehicle sensor readings, stores
them in SQLite, and exposes them through a FastAPI service.

## Setup

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

## Run

Print one sensor summary without GPS coordinates:

```powershell
python -m telemetry
```

Start the API:

```powershell
uvicorn telemetry.api:app --reload
```

The API is available at `http://127.0.0.1:8000`. Use `POST /telemetry/generate`
to generate and store a reading, `GET /telemetry/latest` for the newest reading,
and `GET /telemetry?limit=50` for recent history. Interactive API docs are at
`/docs`. Set `TELEMETRY_DB_PATH` to change the SQLite database location.

## Test

```powershell
pytest
```

All vehicle and GPS values are simulated. Do not use this demo with real vehicle
or driver data.