#!/bin/sh
alembic revision --autogenerate -m "Migration - $(date +%F_%H-%M-%S)"
alembic upgrade head   