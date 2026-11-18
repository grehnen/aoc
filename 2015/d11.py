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


def string_to_nums(string: str) -> list[int]:
    return [ord(c) for c in string]


def nums_to_string(nums: list[int]) -> str:
    return "".join([chr(c) for c in nums])


def increment_string(input: list[int]):
    for i, c in reversed(list(enumerate(input))):
        if c != ord("z"):
            input[i] += 1
            break
        input[i] = ord("a")
    return input


def rule_1(input: list[int]):
    for n in range(len(input) - 2):
        if input[n] + 1 == input[n + 1] and input[n] + 2 == input[n + 2]:
            return True
    return False


def rule_2(input: list[int]):
    return not {ord("i"), ord("o"), ord("l")}.intersection(set(input))


def rule_3(input: list[int]):
    double_count = 0
    prev = 0
    for c in input:
        if c == prev:
            double_count += 1
            if double_count == 2:
                return True
            prev = 0
            continue
        prev = c
    return False


def solve(input):
    input = increment_string(string_to_nums(input))
    while not (rule_2(input) and rule_3(input) and rule_1(input)):
        input = increment_string(input)

    return nums_to_string(input)


part_1 = solve(file_content[0])
part_2 = solve(part_1)

print(part_1)
print(part_2)
