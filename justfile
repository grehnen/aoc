# Show available recipes
default:
    @just --list

# Run a solution: `just run 2024 12`, `just run -t` for today's, or `just run` for the last modified one
run *args:
    @uv run run-day {{args}}

# Create a new day from the template, e.g. `just new 2025 13`
new year day:
    uv run new-day {{year}} {{day}}

# Lint (with autofix) and format
lint:
    uv run ruff check --fix
    uv run ruff format

# Check lint and formatting without changing files
check:
    uv run ruff check
    uv run ruff format --check
