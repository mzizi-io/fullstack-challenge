#!/bin/sh
pipenv run uvicorn src.main:app --host "0.0.0.0" --port 8000