#!/usr/bin/env python3
"""Connect a Slack-first DIA UNO company agent to Hermes.

Default mode is a dry-run operator plan. Use --apply to run local Hermes
commands and write the Slack/Hermes env block into the selected Hermes profile.
No tokens are accepted as CLI args; export them in the shell or point to a local
.env file outside Git.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = [
    re.compile(r"xox[baprs]-[A-Za-z0-9-]+"),
    re.compile(r"xapp-[A-Za-z0-9-]+"),
    re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]"),
    re.compile(r"-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
]
MANAGED_BEGIN = "# BEGIN DIA UNO SLACK -> HERMES"
MANAGED_END = "# END DIA UNO SLACK -> HERMES"
REQUIRED_SLACK_ENV = ["SLACK_BOT_TOKEN", "SLACK_APP_TOKEN"]
REQUIRED_MEMORY_PATHS = [
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
OPTIONAL_SLACK_ENV = [
    "SLACK_ALLOWED_USERS",
    "SLACK_ALLOWED_CHANNELS",
    "SLACK_HOME_CHANNEL",
    "SLACK_HOME_CHANNEL_NAME",
    "SLACK_REQUIRE_MENTION",
    "SLACK_STRICT_MENTION",
    "SLACK_FREE_RESPONSE_CHANNELS",
]


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 2


def has_secret(value: str) -> bool:
    return any(pattern.search(value or "") for pattern in SECRET_PATTERNS)


def load_env_file(path: Path) -> None:
    """Load KEY=VALUE pairs without printing or validating values."""
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


def run(cmd: list[str], *, apply: bool, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str] | None:
    printable = " ".join(cmd)
    print(("RUN" if apply else "DRY-RUN") + f": {printable}")
    if not apply:
        return None
    return subprocess.run(cmd, text=True, capture_output=True, env=env, timeout=180)


def hermes_bin() -> str | None:
    return shutil.which("hermes")


def profile_exists(profile: str) -> bool:
    if not hermes_bin():
        return False
    result = subprocess.run(["hermes", "profile", "show", profile], text=True, capture_output=True, timeout=60)
    return result.returncode == 0


def profile_home(profile: str) -> Path | None:
    result = subprocess.run(["hermes", "profile", "show", profile], text=True, capture_output=True, timeout=60)
    if result.returncode != 0:
        return None
    for line in result.stdout.splitlines():
        if line.startswith("Path:"):
            return Path(line.split("Path:", 1)[1].strip()).expanduser()
    return None


def memory_readiness_errors(instance: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_MEMORY_PATHS:
        if not (instance / rel).exists():
            errors.append(f"missing private memory path: {rel}")
    for group, keys in REQUIRED_MEMORY_ENV_GROUPS.items():
        if not any(os.getenv(key) for key in keys):
            errors.append(f"missing {group} memory env: one of {', '.join(keys)}")
    gbrain_repo = os.getenv("GBRAIN_REPO_URL", "")
    if gbrain_repo and gbrain_repo.rstrip("/").removesuffix(".git") != CANONICAL_GBRAIN_REPO_URL:
        errors.append(f"wrong gbrain repo: expected {CANONICAL_GBRAIN_REPO_URL}")
    return errors


def upsert_env_block(env_path: Path, values: dict[str, str]) -> None:
    env_path.parent.mkdir(parents=True, exist_ok=True)
    existing = env_path.read_text(encoding="utf-8") if env_path.exists() else ""
    lines = [MANAGED_BEGIN, "# Written by scripts/connect_slack_to_hermes.py. Do not commit this file."]
    for key, value in values.items():
        lines.append(f"{key}={value}")
    lines.append(MANAGED_END)
    block = "\n".join(lines) + "\n"
    pattern = re.compile(re.escape(MANAGED_BEGIN) + r".*?" + re.escape(MANAGED_END) + r"\n?", re.DOTALL)
    if pattern.search(existing):
        new_text = pattern.sub(block, existing)
    else:
        new_text = existing.rstrip() + "\n\n" + block if existing.strip() else block
    env_path.write_text(new_text, encoding="utf-8")
    try:
        env_path.chmod(0o600)
    except OSError:
        pass


def write_private_receipt(instance: Path, profile: str, apply: bool, memory_errors: list[str] | None = None) -> None:
    rel = Path("receipts") / f"{datetime.now(timezone.utc).strftime('%Y-%m-%d')}-slack-hermes-connection.md"
    path = instance / rel
    print(("WRITE" if apply else "DRY-RUN") + f": {path}")
    if not apply:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    memory_block = "- Private memory readiness passed before Slack/Hermes connection."
    if memory_errors:
        formatted = "\n".join(f"- BLOCKED/PENDING: {error}" for error in memory_errors)
        memory_block = f"Memory readiness was explicitly overridden by the human/operator. CEO launch remains paused until these blockers are closed:\n\n{formatted}"
    path.write_text(f"""# Slack -> Hermes Connection Receipt

Date: `{stamp}`
Owner: `operator`
Profile: `{profile}`
Surface: `Slack Socket Mode -> Hermes gateway`

## What changed

The first Slack agent surface was connected to a local Hermes profile and prepared for gateway restart.

## Why

DIA UNO needs the first human-agent conversation to happen in Slack, while memory/receipts/approvals stay in the private company instance.

## Source / provenance

- Script: `scripts/connect_slack_to_hermes.py`
- Integration guide: `integrations/slack-first-agent.md`
- Hermes command: `hermes slack guide`

## Evidence

{memory_block}
- Hermes profile selected: `{profile}`
- Tokens were loaded from local environment or a private env file. Values are intentionally not recorded.
- Gateway status must be verified with `hermes --profile {profile} gateway status` after restart.

## Allowed next actions

- Test a DM to the Slack app.
- Test a mention in the approved Slack channel.
- Record the first safe internal loop receipt.

## Forbidden without approval

- Posting externally or publicly.
- Economic/legal commitments.
- Production/customer data actions beyond approved read-only scope.
- Committing `.env`, tokens or Slack connection secrets.
""", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Install/create Hermes and connect a Slack-first DIA UNO agent to it")
    parser.add_argument("--company-instance", required=True, help="Private generated company instance path")
    parser.add_argument("--profile", required=True, help="Hermes profile name for this company/agent, e.g. acme-ceo")
    parser.add_argument("--env-file", help="Optional private env file with SLACK_BOT_TOKEN/SLACK_APP_TOKEN; never commit it")
    parser.add_argument("--install-hermes", action="store_true", help="If hermes is missing and --apply is set, run pip install hermes-agent && hermes postinstall")
    parser.add_argument("--start-gateway", action="store_true", help="After writing env, restart/start the Hermes gateway for this profile")
    parser.add_argument("--allow-memory-pending", action="store_true", help="Allow Slack/Hermes wiring even if Supabase/Voyage/GBrain readiness is missing; writes the blocker into the receipt")
    parser.add_argument("--apply", action="store_true", help="Run commands and write local files. Without this, only prints the plan")

    if has_secret(" ".join(sys.argv[1:])):
        return fail("Do not pass Slack tokens or secrets as CLI arguments. Use environment variables or --env-file.")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{1,62}", args.profile):
        return fail("--profile must be lowercase and contain only letters, numbers, '_' or '-'")

    instance = Path(args.company_instance).expanduser().resolve()
    if not instance.exists():
        return fail(f"company instance does not exist: {instance}")
    if str(instance).startswith(str(ROOT.resolve())):
        return fail("company instance must be private and outside the public DIA UNO repo")
    if args.env_file:
        env_path = Path(args.env_file).expanduser().resolve()
        if str(env_path).startswith(str(ROOT.resolve())):
            return fail("--env-file must be private and outside the public DIA UNO repo")
        load_env_file(env_path)

    print("DIA UNO Slack -> Hermes connector")
    print(f"Company instance: {instance}")
    print(f"Hermes profile: {args.profile}")
    print("Mode: " + ("APPLY" if args.apply else "DRY-RUN"))

    memory_errors = memory_readiness_errors(instance)
    if memory_errors:
        print("BLOCKER: private memory is not ready for first CEO launch.")
        for error in memory_errors:
            print(f"  - {error}")
        print("Run: python scripts/check_private_memory_readiness.py --company-instance <private-instance> --strict")
        if not args.allow_memory_pending:
            print("Slack/Hermes wiring is paused because GBrain/Supabase/Voyage readiness is pending. Use --allow-memory-pending only with explicit human approval and a blocker receipt.")
            return 1
        print("ALLOW: override acknowledged because --allow-memory-pending was provided; memory remains pending until this blocker is resolved or explicitly approved.")

    if not hermes_bin():
        if not args.install_hermes:
            print("PENDING: Hermes is not installed. Rerun with --install-hermes --apply, or install manually:")
            print("  python -m pip install --upgrade hermes-agent && hermes postinstall")
            return 1
        result = run([sys.executable, "-m", "pip", "install", "--upgrade", "hermes-agent"], apply=args.apply)
        if result is not None and result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            return result.returncode
        result = run(["hermes", "postinstall"], apply=args.apply)
        if result is not None and result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            return result.returncode

    if not profile_exists(args.profile):
        # Dry-run marker: hermes profile create
        result = run([
            "hermes", "profile", "create", args.profile,
            "--description", "DIA UNO company Slack-first agent runtime."
        ], apply=args.apply)
        if result is not None and result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            return result.returncode
    else:
        print(f"OK: Hermes profile exists: {args.profile}")

    missing = [key for key in REQUIRED_SLACK_ENV if not os.getenv(key)]
    if missing:
        print("PENDING: export these Slack values locally before --apply writes the profile .env:")
        for key in missing:
            print(f"  {key}=<from Slack app>")
        print("Get the Slack app checklist with: hermes slack guide")
        return 1 if args.apply else 0

    values = {key: os.environ[key] for key in REQUIRED_SLACK_ENV}
    for key in OPTIONAL_SLACK_ENV:
        if os.getenv(key):
            values[key] = os.environ[key]
    values.setdefault("SLACK_REQUIRE_MENTION", "true")
    values.setdefault("SLACK_STRICT_MENTION", "true")

    home = profile_home(args.profile) if hermes_bin() else None
    if home:
        print(f"Hermes profile home: {home}")
        env_target = home / ".env"
        print(("WRITE" if args.apply else "DRY-RUN") + f": Slack env block -> {env_target}")
        if args.apply:
            upsert_env_block(env_target, values)
    else:
        print("PENDING: profile path not available until the profile exists")

    write_private_receipt(instance, args.profile, args.apply, memory_errors if args.allow_memory_pending else None)

    if args.start_gateway:
        result = run(["hermes", "--profile", args.profile, "gateway", "restart"], apply=args.apply)
        if result is not None and result.returncode != 0:
            # First install/start if restart cannot find an installed service.
            print("Gateway restart did not succeed; trying install + start for this profile.")
            run(["hermes", "--profile", args.profile, "gateway", "install"], apply=args.apply)
            run(["hermes", "--profile", args.profile, "gateway", "start"], apply=args.apply)
    else:
        print(f"NEXT: hermes --profile {args.profile} gateway restart")
        print(f"VERIFY: hermes --profile {args.profile} gateway status")

    print("DONE: Slack is ready to connect directly to Hermes once the gateway is running.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
