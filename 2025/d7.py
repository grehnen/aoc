from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats
from functools import cache

file_content: List[str] = fetch_input(__file__)

example = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "...............",
]

RIGHT = Vector2.RIGHT
LEFT = Vector2.LEFT
DOWN = Vector2.DOWN


def solve_1(grid: Grid, start):
    count = 0
    to_check = {start + DOWN}
    already_checked = set()
    while to_check:
        pos = to_check.pop()
        if pos not in grid:
            continue
        cell = grid[pos]
        if cell == "^":
            count += 1
            checkable = {pos + LEFT, pos + RIGHT}
            checkable.difference_update(already_checked)
            for c in checkable:
                to_check.add(c)
        elif pos + DOWN not in already_checked:
            to_check.add(pos + DOWN)
        already_checked.update(to_check)

    return count


@cache
def solve_2(grid: Grid, position: Coord2) -> int:
    if position.y >= grid.height:
        return 1
    if grid[position] == "^":
        return solve_2(grid, position + LEFT) + solve_2(grid, position + RIGHT)
    else:
        return solve_2(grid, position + DOWN)


grid = Grid(file_content)
start = grid.find("S")

print(solve_1(grid, start))
print(solve_2(grid, start))
