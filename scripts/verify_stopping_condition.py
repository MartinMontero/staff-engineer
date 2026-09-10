#!/usr/bin/env python3
"""Execute a sprint's machine-checkable stopping condition.

Reads sprints/<id>/stopping-condition.md, extracts the first ```bash fenced
code block, and runs it with the repository root as the working directory.
The exit code of the command IS the verdict: 0 = PASS, nonzero = FAIL.

Usage:
    python3 scripts/verify_stopping_condition.py --sprint <sprint-id>

Exit codes:
    0        stopping condition command exited 0 (PASS)
    nonzero  whatever the stopping condition command returned (FAIL)
    2        refused: no stopping-condition.md or no bash block found
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SPRINTS_DIR = REPO_ROOT / "sprints"

BASH_BLOCK_RE = re.compile(r"```bash\s*\n(.*?)```", re.DOTALL)


def main():
    parser = argparse.ArgumentParser(
        description="Execute a sprint's stopping condition.")
    parser.add_argument("--sprint", required=True, help="Sprint id")
    args = parser.parse_args()

    sc_path = SPRINTS_DIR / args.sprint / "stopping-condition.md"
    if not sc_path.is_file():
        sys.stderr.write(
            f"REFUSED: no stopping condition found at {sc_path}\n")
        return 2

    text = sc_path.read_text(encoding="utf-8")
    match = BASH_BLOCK_RE.search(text)
    if not match:
        sys.stderr.write(
            "REFUSED: no ```bash fenced block found in "
            f"{sc_path}. The stopping condition must be machine-checkable.\n")
        return 2

    command = match.group(1).strip()
    if not command:
        sys.stderr.write("REFUSED: bash block is empty.\n")
        return 2

    print(f"Executing stopping condition for sprint '{args.sprint}':")
    print(f"  {command}\n")
    result = subprocess.run(command, shell=True, cwd=REPO_ROOT)
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
