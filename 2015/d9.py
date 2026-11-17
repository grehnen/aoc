import re
from itertools import permutations
from math import inf, prod

from aoc_utils import (
    Coord2,
    Coord3,
    Grid,
    Vector2,
    Vector3,
    fetch_input,
    floats,
    ints,
)

file_content: list[str] = fetch_input(__file__)


def parse():
    distances: dict[frozenset, int] = {}
    locations: set[str] = set()
    for line in file_content:
        loc1, loc2 = re.findall(r"[A-Z][A-Za-z]*", line)
        locations.update([loc1, loc2])
        (dist,) = ints(line)
        distances[frozenset({loc1, loc2})] = dist
    return (distances, locations)


def solve():
    min_dist = inf
    max_dist = 0
    distances, locations = parse()
    for p in permutations(locations):
        dist = 0
        for i in range(len(p) - 1):
            dist += distances[frozenset({p[i], p[i + 1]})]
        min_dist = min(dist, min_dist)
        max_dist = max(dist, max_dist)

    return min_dist, max_dist


print(solve())
