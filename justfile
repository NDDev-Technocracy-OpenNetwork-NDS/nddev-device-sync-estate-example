set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

setup:
    uv sync --locked

check:
    uv run --locked python scripts/check.py

render:
    uv run --locked python scripts/check.py --render
