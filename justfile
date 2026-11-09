set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

setup:
    git submodule update --init --recursive --jobs 2
    uv sync --locked

check:
    just --fmt --check
    uv run --locked --offline python scripts/check.py

render:
    uv run --locked python scripts/check.py --render

# Validate the complete synthetic installation configuration.
verify: check
