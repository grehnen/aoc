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


def solve_1():
    ROW, COLUMN = ints(file_content[0])
    N = int(((((COLUMN - 1) + ROW) * ((COLUMN - 1) + ROW + 1)) / 2) - ROW)
    TERM = 252533
    MODULO = 33554393

    value = 20151125
    value_dict: dict[int, int] = {}
    for i in range(1, N + 1):
        value = (value * TERM) % MODULO
        if value in value_dict:
            n = (N - value_dict[value]) % (i - value_dict[value])
            break
        value_dict[value] = i

    for i in range(n):
        value = (value * TERM) % MODULO

    return value


def solve_2():
    count = 0

    return count


print(solve_1())
print(solve_2())
