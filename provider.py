"""Add or remove a provider (one key and the models it serves) in one agent.

    python provider.py add <agent> <label> --provider <pkg> --base-url <url> --key <ENV_VAR> --models <name> [<name> ...]
    python provider.py remove <agent> <label>

A provider is one block in agents/<agent>/base_settings.json plus one KEY= line in agents/<agent>/.env,
joined by the variable name in the block's "key". add writes both (the .env line blank, for the user to fill);
remove deletes both. Nothing from .env is ever printed, only the variable name.
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def paths(agent):
    folder = os.path.join(ROOT, "agents", agent)
    if not os.path.isdir(folder):
        sys.exit(f"no agent folder at agents/{agent}")
    return os.path.join(folder, "base_settings.json"), os.path.join(folder, ".env")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save(path, settings):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")


def env_names(path):
    """The variable names in a .env file, nothing else."""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [line.split("=", 1)[0].strip() for line in f if "=" in line and not line.lstrip().startswith("#")]


def env_append(path, name):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{name}=\n")


def env_remove(path, name):
    """Drop the line for `name`, whatever its value. Every other line stays byte for byte."""
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(line for line in lines if line.split("=", 1)[0].strip() != name)


def add(args):
    settings_path, env_path = paths(args.agent)
    settings = load(settings_path)
    providers = settings.setdefault("providers", {})
    if args.label in providers:
        sys.exit(f"{args.agent}: provider '{args.label}' already exists")
    for label, block in providers.items():
        taken = set(block["models"]) & set(args.models)
        if taken:
            sys.exit(f"{args.agent}: {sorted(taken)} already listed under '{label}'; a model belongs to one provider")
        if block["key"] == args.key:
            sys.exit(f"{args.agent}: {args.key} is already used by '{label}'; one key per provider")
    providers[args.label] = {"provider": args.provider, "base_url": args.base_url, "key": args.key, "models": args.models}
    save(settings_path, settings)
    note = ""
    if args.key not in env_names(env_path):
        env_append(env_path, args.key)
        note = f", {args.key} is blank in .env"
    req = os.path.join(ROOT, "requirements.txt")
    package = "langchain-" + args.provider.replace("_", "-")
    if not os.path.exists(req) or package not in open(req, encoding="utf-8").read():
        note += f"; {package} is not in requirements.txt at the repo root"
    print(f"{args.agent}: added {args.label}{note}")


def remove(args):
    settings_path, env_path = paths(args.agent)
    settings = load(settings_path)
    providers = settings.get("providers", {})
    if args.label not in providers:
        sys.exit(f"{args.agent}: no provider '{args.label}'")
    key = providers.pop(args.label)["key"]
    save(settings_path, settings)
    still_used = any(block["key"] == key for block in providers.values())
    if still_used:
        print(f"{args.agent}: removed {args.label}; {key} stays in .env, another provider uses it")
        return
    env_remove(env_path, key)
    print(f"{args.agent}: removed {args.label} and {key}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("add")
    a.add_argument("agent")
    a.add_argument("label")
    a.add_argument("--provider", required=True, help="the LangChain provider: anthropic, openai, ...")
    a.add_argument("--base-url", default="", help="the endpoint; empty for the provider's own")
    a.add_argument("--key", required=True, help="the .env variable that holds the secret, never the value")
    a.add_argument("--models", required=True, nargs="+", help="the model names this key serves")
    a.set_defaults(run=add)
    r = sub.add_parser("remove")
    r.add_argument("agent")
    r.add_argument("label")
    r.set_defaults(run=remove)
    args = p.parse_args()
    args.run(args)
