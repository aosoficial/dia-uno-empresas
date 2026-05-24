#!/usr/bin/env python3
"""Check that private memory exists before launching the first DIA UNO agent.

This script is read-only by default. It does not connect to Supabase/Voyage/GBrain
or print secrets; it verifies that the private company instance and local runtime
environment expose the minimum memory contract the Slack/Hermes agent needs.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_INSTANCE_PATHS = [
    "company/company-brain.md",
    "company/source-of-truth-map.md",
    "company/approval-boundaries.md",
    "context-packets",
    "statechanges",
    "receipts",
]
REQUIRED_MEMORY_ENV_GROUPS = {
    "supabase": ["SUPABASE_URL"],
    "voyage": ["VOYAGE_API_KEY"],
    "gbrain-source": ["GBRAIN_REPO_URL"],
    "gbrain-access": ["GBRAIN_COMMAND", "GBRAIN_MCP_SERVER", "GBRAIN_MCP_NAME", "GBRAIN_PROJECT_ID"],
}
CANONICAL_GBRAIN_REPO_URL = "https://github.com/garrytan/gbrain"
OPTIONAL_MEMORY_ENV = [
    "SUPABASE_PROJECT_REF",
    "SUPABASE_SCHEMA",
    "SUPABASE_ANON_KEY",
    "SUPABASE_SERVICE_ROLE_KEY",
    "DATABASE_URL",
    "VOYAGE_MODEL",
    "GBRAIN_INSTALL_DIR",
    "GBRAIN_NAMESPACE",
    "GBRAIN_COMPANY_ID",
]


def load_env_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(path)
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def env_present(name: str) -> bool:
    return bool(os.getenv(name, "").strip())


def masked_status(name: str) -> str:
    return "set" if env_present(name) else "missing"


def check_instance(instance: Path) -> list[str]:
    errors: list[str] = []
    if not instance.exists():
        return [f"company instance does not exist: {instance}"]
    if str(instance.resolve()).startswith(str(ROOT.resolve())):
        return ["company instance must be private and outside the public DIA UNO repo"]
    for rel in REQUIRED_INSTANCE_PATHS:
        if not (instance / rel).exists():
            errors.append(f"missing private memory path: {rel}")
    return errors


def check_env() -> list[str]:
    errors: list[str] = []
    for group, keys in REQUIRED_MEMORY_ENV_GROUPS.items():
        if not any(env_present(key) for key in keys):
            errors.append(f"missing {group} memory env: one of {', '.join(keys)}")
    gbrain_repo = os.getenv("GBRAIN_REPO_URL", "")
    if gbrain_repo and gbrain_repo.rstrip("/").removesuffix(".git") != CANONICAL_GBRAIN_REPO_URL:
        errors.append(f"wrong gbrain repo: expected {CANONICAL_GBRAIN_REPO_URL}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only preflight for Supabase/Voyage/GBrain memory readiness")
    parser.add_argument("--company-instance", required=True, help="Private generated company instance path")
    parser.add_argument("--env-file", help="Optional private env file outside Git; values are never printed")
    parser.add_argument("--strict", action="store_true", help="Return non-zero if any memory prerequisite is missing")
    args = parser.parse_args()

    instance = Path(args.company_instance).expanduser().resolve()
    if args.env_file:
        env_path = Path(args.env_file).expanduser().resolve()
        if str(env_path).startswith(str(ROOT.resolve())):
            print("ERROR: --env-file must be private and outside the public DIA UNO repo", file=sys.stderr)
            return 2
        load_env_file(env_path)

    print("DIA UNO private memory readiness check")
    print(f"Company instance: {instance}")
    print("Mode: read-only")

    errors = check_instance(instance) + check_env()

    print("\nMemory env status:")
    for group, keys in REQUIRED_MEMORY_ENV_GROUPS.items():
        statuses = ", ".join(f"{key}={masked_status(key)}" for key in keys)
        print(f"- {group}: {statuses}")
    optional_set = [key for key in OPTIONAL_MEMORY_ENV if env_present(key)]
    print(f"- optional memory env set: {len(optional_set)}")

    if errors:
        print("\nNOT READY: private memory is not ready for CEO launch.")
        for error in errors:
            print(f"- {error}")
        print("\nNext safe action: configure Supabase/Postgres, Voyage and GBrain in private env/runtime, then rerun this check or record memory as pending in the company receipt.")
        return 1 if args.strict else 0

    print("\nREADY: private instance + Supabase/Voyage/GBrain env contract are present. You can wire Slack -> Hermes and launch the CEO with receipts/statechanges enabled.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
