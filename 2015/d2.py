from typing import List, Tuple
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats, Vector3, Coord3

file_content: List[str] = fetch_input(__file__)


def solve_1(dims: List[Tuple[int, int, int]]):
    count = 0
    for dim in dims:
        l, w, h = dim
        count += (
            (2 * l * w) + (2 * w * h) + (2 * l * h) + min((l * w), (w * h), (l * h))
        )

    return count


def solve_2(dims: List[Tuple[int, int, int]]):
    count = 0
    for dim in dims:
        l, w, h = dim
        count += min((2 * l + 2 * w), (2 * h + 2 * w), (2 * l + 2 * h)) + l * w * h

    return count


dimensions: List[Tuple[int, int, int]] = []
for line in file_content:
    l, w, h = line.split("x")
    dimensions.append((int(l), int(w), int(h)))

print(solve_1(dimensions))
print(solve_2(dimensions))
