import argparse
import sys
from importlib.resources import files
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="new-day", description="Create <year>/d<day>.py from the template."
    )
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    target = Path(f"{args.year}/d{args.day}.py")
    if target.exists():
        sys.exit(f"{target} already exists")

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(files("aoc_utils").joinpath("template.py").read_text())
    print(f"Created {target}")
