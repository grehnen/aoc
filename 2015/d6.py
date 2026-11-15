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


def solve_1():
    grid: Grid[bool] = Grid.filled(1000, 1000, False)
    for line in file_content:
        x1, y1, x2, y2 = ints(line)
        corner_1 = Coord2(x1, y1)
        corner_2 = Coord2(x2, y2)
        if line.startswith("turn off"):
            new_value = False
        elif line.startswith("turn on"):
            new_value = True
        else:
            new_value = None

        for coord in Coord2.get_square_members(corner_1, corner_2, True):
            if new_value == None:
                grid[coord] = not grid[coord]
            else:
                grid[coord] = new_value

    return grid.count(True)


def solve_2():
    grid = Grid.filled(1000, 1000, 0)
    for line in file_content:
        x1, y1, x2, y2 = ints(line)
        corner_1 = Coord2(x1, y1)
        corner_2 = Coord2(x2, y2)

        if line.startswith("turn off"):
            modifier = -1
        elif line.startswith("turn on"):
            modifier = 1
        else:
            modifier = 2

        for coord in Coord2.get_square_members(corner_1, corner_2, True):
            grid[coord] = max(grid[coord] + modifier, 0)

    return sum(value for _, value in grid)


print(solve_1())
print(solve_2())
