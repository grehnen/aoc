from aoc_utils import Coord2, Coord3, Grid, Vector2, Vector3, fetch_input, floats, ints

file_content: list[str] = fetch_input(__file__)


def solve_1(dims: list[tuple[int, int, int]]):
    count = 0
    for dim in dims:
        l, w, h = dim
        count += (
            (2 * l * w) + (2 * w * h) + (2 * l * h) + min((l * w), (w * h), (l * h))
        )

    return count


def solve_2(dims: list[tuple[int, int, int]]):
    count = 0
    for dim in dims:
        l, w, h = dim
        count += min((2 * l + 2 * w), (2 * h + 2 * w), (2 * l + 2 * h)) + l * w * h

    return count


dimensions: list[tuple[int, int, int]] = []
for line in file_content:
    l, w, h = line.split("x")
    dimensions.append((int(l), int(w), int(h)))

print(solve_1(dimensions))
print(solve_2(dimensions))
