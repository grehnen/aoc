# Advent of Code

## Usage

Run a day:

```sh
just run 2024 12
```

Create a new day from the template (`src/aoc_utils/template.py`):

```sh
just new 2025 13
```

Lint and format:

```sh
just lint
```

Check lint and formatting without changing files:

```sh
just check
```

## Setup

1. Install [uv](https://docs.astral.sh/uv/):

   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install [just](https://just.systems/):

   ```sh
   brew install just
   ```

3. Create the virtual environment (uv downloads the pinned Python if needed):

   ```sh
   uv sync
   ```

4. Put your adventofcode.com session cookie in `.env` at the repo root, so
   inputs can be downloaded:

   ```sh
   SESSION_COOKIE=...
   ```
