# Advent of Code

## Usage

Run a day:

```sh
just run          # run last modified solution file
just run -t       # today's solution file
just run 2025 1   # run solution file for year 2025, day 1
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

<details>
<summary>Console snippet</summary>

```js
(() => {
  const next = new Date();
  next.setUTCHours(5, 0, 1, 0); // 00:00:01 US Eastern = puzzle unlock (+1 s margin)
  if (next <= new Date()) next.setUTCDate(next.getUTCDate() + 1);
  const title = document.title;
  const pad = (n) => String(n).padStart(2, "0");
  const timer = setInterval(() => {
    const left = next - Date.now();
    if (left <= 0) {
      clearInterval(timer);
      location.reload();
      return;
    }
    const s = Math.ceil(left / 1000);
    document.title = `${title} (${Math.floor(s / 3600)}:${pad(Math.floor(s / 60) % 60)}:${pad(s % 60)} until unlock)`;
  }, 1000);
  console.log(`Reloading at ${next.toLocaleString()}`);
})();
```

</details>

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
