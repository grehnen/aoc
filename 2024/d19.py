from collections import defaultdict
from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats

file_content: List[str] = fetch_input(__file__)
towels: dict[int, set[str]] = defaultdict(set)

for towel in file_content[0].split(", "):
    towels[len(towel)].add(towel)


sum_a = 0
sum_b = 0
pattern_valid = False
for pattern in file_content[2:]:
    valid_lengths = defaultdict(int)
    valid_lengths[0] = 1
    for i in range(len(pattern)):
        if not valid_lengths[i]:
            continue
        for j in towels:
            if i + j > len(pattern):
                continue
            if pattern[i : i + j] in towels[j]:
                if i + j == len(pattern):
                    sum_b += valid_lengths[i]
                    pattern_valid = True
                    continue
                valid_lengths[i + j] += valid_lengths[i]
    if pattern_valid:
        sum_a += 1
    pattern_valid = False


print(sum_a)
print(sum_b)
