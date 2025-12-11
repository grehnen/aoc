from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats, Vector3, Coord3
from functools import cache

file_content: List[str] = fetch_input(__file__)


mapping_1 = {}
mapping_2 = {}


@cache
def solve_1(key):
    count = 0
    if key == "out":
        return 1
    for value in mapping_1[key]:
        count += solve_1(value)

    return count


@cache
def solve_2(key, fft, dac):
    count = 0
    if key == "out":
        if fft and dac:
            return 1
        return 0
    for value in mapping_2[key]:
        if value == "fft":
            count += solve_2(value, True, dac)
        elif value == "dac":
            count += solve_2(value, fft, True)
        else:
            count += solve_2(value, fft, dac)

    return count


if __name__ == "__main__":
    example = [
        "aaa: you hhh",
        "you: bbb ccc",
        "bbb: ddd eee",
        "ccc: ddd eee fff",
        "ddd: ggg",
        "eee: out",
        "fff: out",
        "ggg: out",
        "hhh: ccc fff iii",
        "iii: out",
    ]

    example_2 = [
        "svr: aaa bbb",
        "aaa: fft",
        "fft: ccc",
        "bbb: tty",
        "tty: ccc",
        "ccc: ddd eee",
        "ddd: hub",
        "hub: fff",
        "eee: dac",
        "dac: fff",
        "fff: ggg hhh",
        "ggg: out",
        "hhh: out",
    ]

    def map_line(input, mapping):
        split = input.split(": ")
        key = split[0]
        values = split[1].split()
        mapping[key] = values

    for line in file_content:
        map_line(line, mapping_1)

    for line in file_content:
        map_line(line, mapping_2)

    print(solve_1("you"))
    print(solve_2("svr", False, False))
