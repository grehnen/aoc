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


def check_string(string: str):
    vowels = "aeiou"
    v_c = 0
    for v in vowels:
        v_c += string.count(v)
    if v_c < 3:
        return False

    forbidden = ["ab", "cd", "pq", "xy"]
    for f in forbidden:
        if f in string:
            return False

    check_2 = False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            check_2 = True
            break
    return check_2


def check_string_2(string: str):
    check_1 = False
    for i in range(len(string) - 1):
        if string.count(string[i] + string[i + 1]) > 1:
            check_1 = True
            break
    if not check_1:
        return False

    check_2 = False
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            check_2 = True
            break
    return check_2


def solve_1():
    count = 0
    for string in file_content:
        count += 1 if check_string(string) else 0

    return count


def solve_2():
    count = 0
    for string in file_content:
        count += 1 if check_string_2(string) else 0
    return count


print(solve_1())
print(solve_2())
