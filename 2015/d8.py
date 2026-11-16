import re
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
    char_count = sum(len(line) for line in file_content)
    mem_count = 0
    for line in file_content:
        line = line.replace("\\\\", "@")
        line = line.replace('\\"', "@")
        mem_len = len(line) - (len(re.findall(r"\\x[a-f0-9][a-f0-9]", line)) * 3) - 2
        mem_count += mem_len

    return char_count - mem_count


def solve_2():
    char_count = sum(len(line) for line in file_content)
    encode_count = 0
    for line in file_content:
        line = line.replace("\\", "@@")
        line = line.replace('"', "@@")
        encode_len = len(line) - (len(re.findall(r"\\x[a-f0-9][a-f0-9]", line)) * 3) + 2
        encode_count += encode_len

    return encode_count - char_count


print(solve_1())
print(solve_2())
