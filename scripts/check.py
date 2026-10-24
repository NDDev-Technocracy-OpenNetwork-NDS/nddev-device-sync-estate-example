"""Validate synthetic inputs against the exact public server Compose source."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "modules/server"
PUBLIC = "https://github.com/NDDev-Technocracy-OpenNetwork-NDS/nddev-device-sync-server.git"


def git(*arguments):
    return subprocess.check_output(
        ["git", *arguments], cwd=ROOT, text=True, timeout=15
    ).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render", action="store_true")
    args = parser.parse_args()
    assert git("config", "-f", ".gitmodules", "submodule.modules/server.url") == PUBLIC
    selected = git("ls-files", "--stage", "modules/server").split()
    assert selected[0] == "160000" and selected[2] == "0"
    commit = selected[1]
    actual = git("-C", str(SOURCE), "rev-parse", "HEAD")
    assert actual == commit, "Initialize the exact server Gitlink"
    assert not git("-C", str(SOURCE), "status", "--porcelain"), "Preserve modified source"
    lock = tomllib.loads((ROOT / "standarts.lock").read_text())
    assert lock["source_repo"] == "NDDev-Technocracy-OpenNetwork-NDS/nddev-device-sync"
    assert lock["license"] == "AGPL-3.0-only"
    values = dict(
        line.split("=", 1)
        for line in (ROOT / "config/example.env").read_text().splitlines()
        if line and not line.startswith("#")
    )
    assert values["NDS_PUBLIC_HOST"] == "nds.example.invalid"
    assert values["NDS_PUBLIC_ORIGIN"] == "https://nds.example.invalid"
    assert values["NDS_HTTPS_BIND"] == "127.0.0.1"
    assert values["NDS_SECRETS_DIRECTORY"] == "/run/nds-example/secrets"
    assert values["NDS_TLS_DIRECTORY"] == "/run/nds-example/tls"
    # The Gitlink owns the source identity. No second SHA ledger in env files.
    environment = {k: v for k, v in os.environ.items() if not k.startswith("NDS_")}
    environment["NDS_SOURCE_COMMIT"] = commit
    command = [
        "docker", "compose", "--project-directory", str(SOURCE),
        "--env-file", str(ROOT / "config/example.env"),
        "-f", str(SOURCE / "compose.yaml"), "config", "--format", "json",
    ]
    configured = json.loads(subprocess.check_output(command, env=environment, timeout=30))
    server = configured["services"]["nddev-sync-server"]
    assert server["build"]["args"]["NDS_SOURCE_COMMIT"] == commit
    assert len(server["ports"]) == 1
    port = server["ports"][0]
    assert (port["host_ip"], port["target"], port["published"], port["protocol"]) == (
        "127.0.0.1", 8443, "443", "tcp",
    ), "The example must stay on loopback"
    assert server["read_only"] and server["cap_drop"] == ["ALL"]
    assert configured["networks"]["database"]["internal"]
    assert "@sha256:" in configured["services"]["postgres"]["image"]
    assert configured["services"]["migrate"]["secrets"][0]["source"] == "migration_database_url"
    assert server["environment"]["DATABASE_URL_FILE"] == "/run/secrets/runtime_database_url"
    if args.render:
        print(json.dumps(configured, indent=2))
    else:
        print("Synthetic inputs and exact upstream Compose configuration valid; no services started.")


if __name__ == "__main__":
    main()
