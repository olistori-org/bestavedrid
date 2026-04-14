#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def require_command(command: str, install_hint: str) -> None:
    if shutil.which(command) is None:
        raise RuntimeError(f"{command} is required but not installed. {install_hint}")


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    print("Bootstrapping Besta Vedrid development environment...")

    require_command("node", "See https://nodejs.org")
    require_command("pnpm", "Install it with `npm install -g pnpm`")

    print("Installing dependencies...")
    run(["pnpm", "install"])

    env_file = ROOT / ".env"
    env_example = ROOT / ".env.example"
    if not env_file.exists() and env_example.exists():
        print("Creating .env from .env.example...")
        env_file.write_text(env_example.read_text(encoding="utf-8"), encoding="utf-8")
        print("Please update .env with your configuration before starting services.")

    print("Bootstrap complete. Run `pnpm dev` to start development.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)