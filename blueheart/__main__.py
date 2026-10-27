"""Read-only CLI. Reports are written only by an explicit shell redirect."""
import argparse
import json
from pathlib import Path
from .io import Invalid, loads
from .workspace import Workspace


def main():
    parser = argparse.ArgumentParser(description="Blue Heart DS · núcleo determinista")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("check", "manifest", "describe"): commands.add_parser(name)
    context = commands.add_parser("context"); context.add_argument("id"); context.add_argument("--version")
    context.add_argument("--intent", choices=["rules", "dependencies", "evidence"], default="rules")
    context.add_argument("--max-bytes", type=int)
    context.add_argument("--compact", action="store_true")
    context.add_argument("--modes", default="{}")
    resolve = commands.add_parser("resolve-token"); resolve.add_argument("id"); resolve.add_argument("--modes", default="{}")
    impact = commands.add_parser("impact"); impact.add_argument("paths", nargs="+")
    qa = commands.add_parser("qa-plan"); qa.add_argument("--change", required=True,
        choices=["editorial", "contract", "token", "adapter", "tooling", "evidence"]); qa.add_argument("paths", nargs="+")
    args = parser.parse_args()
    try:
        workspace = Workspace(args.root.resolve())
        if args.command == "check": result = workspace.check()
        elif args.command == "manifest": result = workspace.snapshot()
        elif args.command == "context": result = workspace.context(args.id, args.version, args.intent, args.max_bytes, args.compact, loads(args.modes))
        elif args.command == "resolve-token":
            modes = loads(args.modes)
            if not isinstance(modes, dict): raise Invalid("Mode context must be an object")
            result = {"status": "PASS", **workspace.tokens.resolve(args.id, modes)}
        elif args.command == "impact": result = workspace.impact(args.paths)
        elif args.command == "qa-plan": result = workspace.qa_plan(args.change, args.paths)
        else:
            policy = workspace.policy
            print("# Blue Heart DS · capacidades derivadas de configuración\n")
            print("Fase: " + policy["phase"] + "\n")
            for module, purpose in policy["module_ownership"].items(): print("- " + module + ": " + purpose)
            print("\nPerfiles permitidos: " + ", ".join(policy["allowed_contract_profiles"]))
            print("\nCapas permitidas: " + ", ".join(policy["allowed_token_layers"]))
            print("\nDiferido: " + ", ".join(policy["deferred"]))
            print("\nNormas registradas: " + str(len(workspace.contracts)) + "; tokens: " + str(len(workspace.tokens.tokens)))
            return 0
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False))
        return 2 if result.get("status") == "BLOCKED" else 1 if result.get("status") == "REVIEW_REQUIRED" else 0
    except (Invalid, OSError, KeyError, TypeError, UnicodeError, RecursionError) as error:
        print(json.dumps({"status": "BLOCKED", "reason": str(error)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
