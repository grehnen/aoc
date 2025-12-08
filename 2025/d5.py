from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats

file_content: List[str] = fetch_input(__file__)

example = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32",
]

def massage(input: List[str]):
    empty_line_index = input.index("")
    fresh_ingredients = input[:empty_line_index]
    available_ingredients = input[empty_line_index + 1 :]

    fresh_ranges: List[range] = []
    for line in fresh_ingredients:
        start, end = line.split("-")
        fresh_ranges.append(range(int(start), int(end)))
    return available_ingredients, fresh_ranges


def solve_1(available_ingredients: List[str], fresh_ranges: List[range]):
    count = 0
    for ingredient in available_ingredients:
        for r in fresh_ranges:
            if int(ingredient) in r:
                count += 1
                break

    return count


def solve_2(fresh_ranges: List[range]):
    count = 0
    fresh_ranges.sort(key=lambda r: r.start)
    merged_ranges: List[range] = []
    for i in range(len(fresh_ranges)):
        line = fresh_ranges[i]
        next_index = i + 1
        if next_index >= len(fresh_ranges):
            merged_ranges.append(line)
            break
        next_line = fresh_ranges[next_index]

        if line.stop >= next_line.start:
            fresh_ranges[i + 1] = range(line.start, max(line.stop, next_line.stop))
        else:
            merged_ranges.append(line)

    for line in merged_ranges:
        count += line.stop - line.start + 1

    return count


available_ingredients, fresh_ranges = massage(file_content)
print(solve_1(available_ingredients, fresh_ranges))
print(solve_2(fresh_ranges))
