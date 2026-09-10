#!/usr/bin/env python3
"""Guardrail check: scan src/** for forbidden secret patterns.

Reads .staff-engineer/guardrails.yaml, compiles secrets.forbid_patterns as
regexes, and scans every file under src/ recursively. Any hit is printed to
stderr and causes a nonzero exit.

Usage:
    python3 scripts/guardrail_check.py

Exit codes:
    0  clean ("OK: no guardrail violations")
    1  at least one violation found
    2  configuration error (missing pyyaml or guardrails.yaml)
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("ERROR: pyyaml is required (pip install pyyaml)\n")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
GUARDRAILS_PATH = REPO_ROOT / ".staff-engineer" / "guardrails.yaml"
SRC_DIR = REPO_ROOT / "src"


def load_forbidden_regexes():
    with open(GUARDRAILS_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    patterns = config.get("secrets", {}).get("forbid_patterns", [])
    return [re.compile(p) for p in patterns]


def scan(regexes):
    violations = []
    if not SRC_DIR.is_dir():
        return violations
    for path in sorted(SRC_DIR.rglob("*")):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            violations.append(f"{path}: unreadable file: {exc}")
            continue
        for rx in regexes:
            for match in rx.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                rel = path.relative_to(REPO_ROOT)
                violations.append(
                    f"{rel}:{line_no}: matches forbidden pattern {rx.pattern!r}"
                )
    return violations


def main():
    regexes = load_forbidden_regexes()
    violations = scan(regexes)
    if violations:
        for v in violations:
            sys.stderr.write(f"VIOLATION: {v}\n")
        return 1
    print("OK: no guardrail violations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
