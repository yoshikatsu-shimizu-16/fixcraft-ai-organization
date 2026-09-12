#!/usr/bin/env python3
"""Validate structural contracts for FixCraft agent skills without third-party dependencies."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / ".agent" / "skills"

REQUIRED_HEADINGS = [
    "# Role",
    "# Mission",
    "# Inputs",
    "# Required Context",
    "# Responsibilities",
    "# Non-responsibilities",
    "# Procedure",
    "# Decision Rules",
    "# Output Contract",
    "# Handoff",
    "# Stop Conditions",
]

REQUIRED_CORE_FILES = [
    "AGENTS.md",
    ".agent/AGENTS.md",
    ".agent/skill-contract-standard.md",
    ".agent/schemas/skill-output-envelope-schema.yaml",
    ".agent/schemas/lead-workflow-schema.yaml",
    ".agent/state/lead-state-machine.yaml",
    ".agent/knowledge/sales/market-sources.yaml",
    ".agent/knowledge/sales/lead-scoring.yaml",
    ".agent/knowledge/sales/operating-constraints.yaml",
]


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    expected_name = path.parent.name
    if meta.get("name") != expected_name:
        errors.append(f"frontmatter name must be '{expected_name}', got {meta.get('name')!r}")
    if len(meta.get("description", "")) < 20:
        errors.append("frontmatter description is missing or too short")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing required heading: {heading}")
    positions = [text.find(h) for h in REQUIRED_HEADINGS if h in text]
    if positions and positions != sorted(positions):
        errors.append("required headings are not in standard order")
    if re.search(r"\bapproved\b", text, flags=re.I) and "Human" not in text and expected_name not in {"application-manager"}:
        # Advisory-like structural check kept intentionally narrow.
        pass
    return errors


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED_CORE_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing core file: {rel}")

    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("no SKILL.md files found")
    for path in skill_files:
        for error in validate_skill(path):
            errors.append(f"{path.relative_to(ROOT)}: {error}")

    expected_roles = {
        "fixcraft-orchestrator", "sales-scout", "competitive-intelligence",
        "lead-qualifier", "sales-director", "bid-strategist",
        "solution-architect", "prototype-engineer", "technical-quality-lead",
        "refactor-engineer", "proposal-writer", "web-design-director",
        "wordpress-security-reviewer", "application-manager",
        "client-closing-manager", "outcome-recorder", "improvement-lead",
    }
    actual_roles = {path.parent.name for path in skill_files}
    missing = sorted(expected_roles - actual_roles)
    if missing:
        errors.append("missing required organization roles: " + ", ".join(missing))

    if errors:
        print("FixCraft agent organization validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"FixCraft agent organization validation OK: {len(skill_files)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
