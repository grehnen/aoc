import hashlib
from math import prod

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


def find_digest_starting_with(prefix: str):
    count = 0
    key = file_content[0]
    digest = ""
    while not digest.startswith(prefix):
        count += 1
        digest = hashlib.md5((key + str(count)).encode(encoding="utf-8")).hexdigest()
    return count


def solve_1():
    return find_digest_starting_with("00000")


def solve_2():
    return find_digest_starting_with("000000")


print(solve_1())
print(solve_2())
