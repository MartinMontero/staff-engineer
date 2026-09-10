#!/usr/bin/env python3
"""Sprint lifecycle state machine.

Reads .staff-engineer/state-machine.yaml, loads (or creates) the sprint's
state.json, and applies a requested transition — refusing anything that is
not a legal next state. Every transition is recorded with actor and ISO
timestamp.

Usage:
    python3 scripts/sprint_lifecycle.py <sprint> --to <STATE> [--actor <name>]

Exit codes:
    0  transition applied and recorded
    1  transition refused (illegal)
    2  configuration error (missing pyyaml or state-machine.yaml)
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("ERROR: pyyaml is required (pip install pyyaml)\n")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_MACHINE_PATH = REPO_ROOT / ".staff-engineer" / "state-machine.yaml"
SPRINTS_DIR = REPO_ROOT / "sprints"


def load_state_machine():
    with open(STATE_MACHINE_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_state(state_path, sprint_id):
    if state_path.is_file():
        with open(state_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"sprint": sprint_id, "state": "BACKLOG", "history": []}


def save_state(state_path, data):
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Apply a sprint state transition.")
    parser.add_argument("sprint", help="Sprint id (directory under sprints/)")
    parser.add_argument("--to", required=True, help="Target state")
    parser.add_argument("--actor", default="master-controller",
                        help="Agent requesting the transition")
    args = parser.parse_args()

    machine = load_state_machine()
    states = machine.get("states", {})

    state_path = SPRINTS_DIR / args.sprint / "state.json"
    data = load_state(state_path, args.sprint)
    current = data.get("state", machine.get("initial", "BACKLOG"))

    legal_next = states.get(current, {}).get("next", [])
    if args.to not in legal_next:
        print(f"REFUSED: {current} -> {args.to} is not a legal transition.")
        print(f"Legal next states from {current}: "
              f"{', '.join(legal_next) if legal_next else '(none — terminal state)'}")
        return 1

    data["state"] = args.to
    data.setdefault("history", []).append({
        "from": current,
        "to": args.to,
        "actor": args.actor,
        "at": datetime.now(timezone.utc).isoformat(),
    })
    save_state(state_path, data)
    print(f"OK: {args.sprint}: {current} -> {args.to} (actor: {args.actor})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
