from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats, Vector3, Coord3

file_content: List[str] = fetch_input(__file__)


def solve_1(string: str):
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

    return count


def solve_2(string: str):
    count = 0
    for i, char in enumerate(string):
        if char == "(":
            count += 1
        else:
            count -= 1

        if count == -1:
            return i + 1


print(solve_1(file_content[0]))
print(solve_2(file_content[0]))
