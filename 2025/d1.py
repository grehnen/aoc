from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats

file_content: List[str] = fetch_input(__file__)

example = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


cur_rot = 50
count = 0
count2 = 0


def left(rot, value: int) -> int:
    return (rot - value) % 100


def right(rot, value: int) -> int:
    return (rot + value) % 100


for line in file_content:
    direction = line[0]
    value = int(line[1:])
    prev = cur_rot
    count2 += value // 100
    if direction == "L":
        cur_rot = left(cur_rot, value)
        if prev < cur_rot and prev != 0 or cur_rot == 0:
            count2 += 1
    else:
        cur_rot = right(cur_rot, value)
        if cur_rot < prev and prev != 0 or cur_rot == 0:
            count2 += 1

    if cur_rot == 0:
        count += 1

print(count)
print(count2)
