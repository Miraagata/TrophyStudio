from __future__ import annotations

import argparse
import json
import sys

from .agent_policy import DEFAULT_POLICY, SYSTEM_RULES
from .agent_tools import compare_files, telemetry_summary


def _emit(obj: dict) -> None:
    json.dump(obj, sys.stdout, ensure_ascii=False, sort_keys=True)
    sys.stdout.write("\n")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="vcng", description="VCNG deterministic agent tools")
    sub = p.add_subparsers(dest="command", required=True)

    cmp_p = sub.add_parser("compare", help="compare two equal-size raw snapshots")
    cmp_p.add_argument("before")
    cmp_p.add_argument("after")
    cmp_p.add_argument("--mode", choices=["changed", "unchanged", "increased", "decreased"], required=True)
    cmp_p.add_argument("--width", type=int, default=4, choices=[1, 2, 4, 8])
    cmp_p.add_argument("--signed", action="store_true")
    cmp_p.add_argument("--float", dest="floating", action="store_true")
    cmp_p.add_argument("--alignment", type=int)
    cmp_p.add_argument("--limit", type=int, default=200)

    tel_p = sub.add_parser("telemetry", help="summarize a 0.14.7 Discovery telemetry TSV")
    tel_p.add_argument("path")

    sub.add_parser("policy", help="print agent safety/validation policy")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "compare":
        _emit(compare_files(
            args.before,
            args.after,
            mode=args.mode,
            width=args.width,
            signed=args.signed,
            floating=args.floating,
            alignment=args.alignment,
            limit=args.limit,
        ))
        return 0
    if args.command == "telemetry":
        _emit(telemetry_summary(args.path))
        return 0
    if args.command == "policy":
        _emit({"policy": DEFAULT_POLICY.__dict__, "system_rules": SYSTEM_RULES})
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
