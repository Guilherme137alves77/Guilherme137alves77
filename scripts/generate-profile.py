#!/usr/bin/env python3
"""
generate-profile.py — Cybersecurity Engineering Lab

Preenche os tokens ({{GITHUB_USERNAME}}, {{LINKEDIN_URL}}, {{PORTFOLIO_URL}}, {{YEAR}})
do README.md usando os valores de scripts/config.json.

Uso:
    python3 scripts/generate-profile.py
    python3 scripts/generate-profile.py --config caminho/para/config.json
"""
import argparse
import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = ROOT / "scripts" / "config.json"
DEFAULT_README = ROOT / "README.md"

TOKENS = ["GITHUB_USERNAME", "LINKEDIN_URL", "PORTFOLIO_URL", "YEAR"]


def load_config(path: pathlib.Path) -> dict:
    if not path.exists():
        print(f"AVISO: config não encontrado em {path} — usando placeholders")
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera o README do perfil GitHub.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="caminho do config.json")
    parser.add_argument("--output", default=str(DEFAULT_README), help="README de saída")
    parser.add_argument("--dry-run", action="store_true", help="mostra os valores sem escrever")
    args = parser.parse_args()

    cfg = load_config(pathlib.Path(args.config))
    text = pathlib.Path(args.output).read_text(encoding="utf-8")

    mapping = {
        "GITHUB_USERNAME": str(cfg.get("github_username") or "your-username"),
        "LINKEDIN_URL": str(cfg.get("linkedin_url") or ""),
        "PORTFOLIO_URL": str(cfg.get("portfolio_url") or ""),
        "YEAR": str(datetime.date.today().year),
    }

    missing = [token for token, value in mapping.items() if not value]

    if args.dry_run:
        for token, value in mapping.items():
            print(f"{token} = {value or '(vazio — ficará como token)'}")
        if missing:
            print("Ajuste estes campos em config.json:", ", ".join(missing))
        return 0

    for token, value in mapping.items():
        text = text.replace("{{" + token + "}}", value)

    pathlib.Path(args.output).write_text(text, encoding="utf-8")

    if missing:
        print("WARN: campos vazios no config.json → tokens mantidos:", ", ".join(missing))
        print("Edite scripts/config.json e rode novamente.")
    else:
        print("OK: README.md gerado com os dados do config.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
