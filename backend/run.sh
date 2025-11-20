#!/usr/bin/env bash
# small helper to run server in dev
export PYTHONPATH=$(pwd)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
