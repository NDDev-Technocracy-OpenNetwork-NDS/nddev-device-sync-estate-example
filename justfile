set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

setup:
    uv sync --locked

check:
    uv run --locked python scripts/check.py

render:
    uv run --locked python scripts/check.py --render

# The checks the former CI library ran from .github/nddev-ci.toml; CI calls them through
# `just test` on a pull request and `just verify` on dev.
verify:
    just check
