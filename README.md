# Advent of Code

## Usage

Run a day:

```sh
uv run 2024/d12.py
```

Create a new day from the template (`src/aoc_utils/template.py`):

```sh
uv run new-day 2025 13
```

Lint and format:

```sh
uv run ruff check
uv run ruff format
```

## Setup

1. Install [uv](https://docs.astral.sh/uv/):

   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create the virtual environment (uv downloads the pinned Python if needed):

   ```sh
   uv sync
   ```

3. Put your adventofcode.com session cookie in `.env` at the repo root, so
   inputs can be downloaded:

   ```sh
   SESSION_COOKIE=...
   ```
