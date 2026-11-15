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
        for coord, value in grid:
            if coord.is_inside_square(corner_1, corner_2, True):
                if line.startswith("turn off"):
                    grid[coord] = False
                elif line.startswith("turn on"):
                    grid[coord] = True
                else:
                    grid[coord] = not grid[coord]

    return grid.count(True)


def solve_2():
    grid = Grid.filled(1000, 1000, 0)
    for line in file_content:
        x1, y1, x2, y2 = ints(line)
        corner_1 = Coord2(x1, y1)
        corner_2 = Coord2(x2, y2)
        for coord, value in grid:
            if coord.is_inside_square(corner_1, corner_2, True):
                if line.startswith("turn off"):
                    grid[coord] = max(value - 1, 0)
                elif line.startswith("turn on"):
                    grid[coord] += 1
                else:
                    grid[coord] += 2

    return sum(value for _, value in grid)


print(solve_1())
print(solve_2())
