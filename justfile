set shell := ["bash", "-euo", "pipefail", "-c"]

# List the source and native validation commands.
default:
    @just --list

# Prepare the existing empty dependency environment without source builds.
setup:
    uv sync --locked --no-build --no-install-project --no-python-downloads

# Check source and synthetic inputs without environment changes or Docker.
check:
    just --fmt --check
    "$(uv python find --no-python-downloads)" -I -B scripts/check.py --source-only

# Retain the exact full Compose validation on the admitted executor.
test:
    "$(uv python find --no-python-downloads)" -I -B scripts/check.py

# Retain full validation and render the selected Compose JSON to stdout.
render:
    "$(uv python find --no-python-downloads)" -I -B scripts/check.py --render

# Run source and the original native Compose contract.
verify: check test

# Format only the maintained command interface.
fix:
    just --fmt
