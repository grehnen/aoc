from typing import List
from utils import fetch_input, ints
from collections import defaultdict

file_content: List[str] = fetch_input(__file__)

starting_stones = ints(file_content[0])
stones = defaultdict(int)


def transform_stone(stone) -> List[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone1 = int(str(stone)[: len(str(stone)) // 2])
        stone2 = int(str(stone)[len(str(stone)) // 2 :])
        return [stone1, stone2]
    else:
        return [stone * 2024]


def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        stone_list = transform_stone(stone)
        for i in stone_list:
            new_stones[i] += count
    return new_stones


for stone in starting_stones:
    stones[stone] += 1

for _ in range(25):
    stones = blink(stones)

print(sum(stones.values()))

for _ in range(50):
    stones = blink(stones)

print(sum(stones.values()))
