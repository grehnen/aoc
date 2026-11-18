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


def solve(part_2=False):
    string = file_content[0]
    for _ in range(50 if part_2 else 40):
        i = 0
        same_count = 0
        current_char = ""
        output = ""
        while i < len(string):
            if same_count == 0:
                same_count += 1
                current_char = string[i]
                i += 1
                continue

            if string[i] == current_char:
                same_count += 1
                i += 1
                continue
            else:
                output += str(same_count) + current_char
                same_count = 0
        output += str(same_count) + current_char
        same_count = 0

        string = output

    return len(string)


print(solve())
print(solve(True))
