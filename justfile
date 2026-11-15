# Show available recipes
default:
    @just --list

# Run a solution, e.g. `just run 2024 12`
run year day:
    uv run {{year}}/d{{day}}.py

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
