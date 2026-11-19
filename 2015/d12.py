import json
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


def sum_obj(obj: object):
    sum = 0
    if isinstance(obj, dict):
        for value in obj.values():
            if value == "red":
                return 0
            sum += sum_obj(value)
    elif isinstance(obj, list):
        for o in obj:
            sum += sum_obj(o)
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0

    return sum


def solve_1():
    return sum(ints(file_content[0]))


def solve_2():
    json_dict = json.loads(file_content[0])

    return sum_obj(json_dict)


print(solve_1())
print(solve_2())
