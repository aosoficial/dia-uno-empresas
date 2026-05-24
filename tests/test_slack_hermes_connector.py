import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "connect_slack_to_hermes.py"
MEMORY_SCRIPT = ROOT / "scripts" / "check_private_memory_readiness.py"


def load_connector():
    spec = importlib.util.spec_from_file_location("connect_slack_to_hermes", SCRIPT)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_slack_hermes_connector_script_exists_and_has_safe_markers():
    text = SCRIPT.read_text(encoding="utf-8")
    for marker in [
        "Slack -> Hermes",
        "SLACK_BOT_TOKEN",
        "SLACK_APP_TOKEN",
        "hermes profile create",
        "gateway restart",
        "memory_readiness_errors",
        "--allow-memory-pending",
        "Do not pass Slack tokens or secrets as CLI arguments",
    ]:
        assert marker in text


def test_connector_rejects_token_like_cli_args(tmp_path):
    instance = tmp_path / "private-company"
    instance.mkdir()
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--company-instance",
            str(instance),
            "--profile",
            "acme-ceo",
            "--not-a-real-token=example-placeholder-only",
        ],
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=60,
    )
    assert result.returncode == 2
    assert "Do not pass Slack tokens" in result.stderr


def test_upsert_env_block_redacts_by_not_printing_and_replaces_block(tmp_path):
    connector = load_connector()
    env_path = tmp_path / ".env"
    env_path.write_text("MODEL_NAME=test\n", encoding="utf-8")
    connector.upsert_env_block(
        env_path,
        {
            "SLACK_BOT_TOKEN": "example-bot-token-value",
            "SLACK_APP_TOKEN": "example-app-token-value",
            "SLACK_ALLOWED_USERS": "U012ABCDEF",
        },
    )
    first = env_path.read_text(encoding="utf-8")
    connector.upsert_env_block(
        env_path,
        {
            "SLACK_BOT_TOKEN": "example-bot-token-value-2",
            "SLACK_APP_TOKEN": "example-app-token-value-2",
        },
    )
    second = env_path.read_text(encoding="utf-8")
    assert "MODEL_NAME=test" in second
    assert second.count(connector.MANAGED_BEGIN) == 1
    assert "SLACK_BOT_TOKEN=example-bot-token-value-2" in second
    assert "SLACK_ALLOWED_USERS=U012ABCDEF" not in second
    assert first != second


def test_memory_readiness_script_blocks_missing_company_memory(tmp_path):
    instance = tmp_path / "private-company"
    instance.mkdir()
    result = subprocess.run(
        [
            sys.executable,
            str(MEMORY_SCRIPT),
            "--company-instance",
            str(instance),
            "--strict",
        ],
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=60,
    )
    assert result.returncode == 1
    assert "NOT READY" in result.stdout
    assert "Supabase/Postgres" in result.stdout
    assert "Voyage" in result.stdout
    assert "GBrain" in result.stdout
    assert "SLACK_BOT_TOKEN" not in result.stdout


def test_connector_blocks_slack_launch_when_memory_is_not_ready(tmp_path):
    instance = tmp_path / "private-company"
    instance.mkdir()
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--company-instance",
            str(instance),
            "--profile",
            "acme-ceo",
        ],
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=60,
    )
    assert result.returncode == 1
    assert "private memory is not ready" in result.stdout
    assert "--allow-memory-pending" in result.stdout


def test_connector_can_plan_with_explicit_memory_pending_override(tmp_path):
    instance = tmp_path / "private-company"
    instance.mkdir()
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--company-instance",
            str(instance),
            "--profile",
            "acme-ceo",
            "--allow-memory-pending",
        ],
        text=True,
        capture_output=True,
        cwd=ROOT,
        timeout=60,
    )
    assert result.returncode == 0
    assert "override acknowledged" in result.stdout
    assert "DRY-RUN" in result.stdout


def test_docs_make_direct_slack_to_hermes_mandatory():
    combined = "\n".join(
        (ROOT / rel).read_text(encoding="utf-8")
        for rel in [
            "README.md",
            "docs/45_slack_first_agent.md",
            "docs/46_orgo_first_company_onboarding.md",
            "docs/47_private_memory_runtime_connections.md",
            "templates/generated-company-instance/integrations/slack-first-agent.md",
        ]
    )
    for marker in [
        "direct Slack -> Hermes",
        "scripts/connect_slack_to_hermes.py",
        "hermes slack guide",
        "hermes slack manifest --write",
        "SLACK_APP_TOKEN",
        "SLACK_ALLOWED_USERS",
        "direct Slack -> Hermes",
        "check_private_memory_readiness.py",
        "Supabase/Voyage/GBrain",
        "https://github.com/garrytan/gbrain",
        "DATABASE_URL",
        "VOYAGE_MODEL",
        "supabase/migrations/001_private_memory_runtime.sql",
    ]:
        assert marker in combined


def test_generic_supabase_memory_migration_exists():
    migration = ROOT / "supabase" / "migrations" / "001_private_memory_runtime.sql"
    text = migration.read_text(encoding="utf-8")
    for marker in [
        "create schema if not exists gbrain",
        "create extension if not exists vector",
        "gbrain.operational_items",
        "context_packet",
        "statechange",
        "receipt",
        "embedding vector(1024)",
        "gbrain_agent",
    ]:
        assert marker in text


def test_public_gbrain_is_canonical():
    combined = "\n".join(
        (ROOT / rel).read_text(encoding="utf-8")
        for rel in [
            "AGENTS.md",
            "README.md",
            "docs/45_slack_first_agent.md",
            "docs/46_orgo_first_company_onboarding.md",
            "docs/47_private_memory_runtime_connections.md",
            "templates/memory-backends/gbrain-mcp.md",
            "templates/generated-company-instance/.env.example",
            "templates/generated-company-instance/integrations/slack-first-agent.md",
            "scripts/check_private_memory_readiness.py",
            "scripts/connect_slack_to_hermes.py",
        ]
    )
    assert "https://github.com/garrytan/gbrain" in combined
    assert "GBRAIN_REPO_URL=https://github.com/garrytan/gbrain" in combined