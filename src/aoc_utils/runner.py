import argparse
import subprocess
import sys
from datetime import date
from pathlib import Path


def last_modified() -> Path:
    solutions = Path().glob("[0-9][0-9][0-9][0-9]/d*.py")
    latest = max(solutions, key=lambda p: p.stat().st_mtime, default=None)
    if latest is None:
        sys.exit("No solution files found")
    return latest


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="run-day",
        description="Run <year>/d<day>.py, or the last modified solution if no day is given.",
    )
    parser.add_argument(
        "-t", "--today", action="store_true", help="run today's solution"
    )
    parser.add_argument("year", type=int, nargs="?")
    parser.add_argument("day", type=int, nargs="?")
    args = parser.parse_args()

    if args.today and args.year is not None:
        parser.error("--today cannot be combined with year/day")
    if args.year is not None and args.day is None:
        parser.error("day is required when year is given")

    if args.today:
        today = date.today()
        target = Path(f"{today.year}/d{today.day}.py")
    elif args.year is not None:
        target = Path(f"{args.year}/d{args.day}.py")
    else:
        target = last_modified()

    if not target.exists():
        sys.exit(f"{target} does not exist (create it with `just new`)")

    print(f"Running {target}", flush=True)
    try:
        result = subprocess.run([sys.executable, target], check=False)
    except KeyboardInterrupt:
        sys.exit(130)
    sys.exit(result.returncode)
