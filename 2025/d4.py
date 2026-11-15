from aoc_utils import Coord2, Grid, Vector2, fetch_input, floats, ints

file_content: list[str] = fetch_input(__file__)


def solve_1(grid: Grid) -> int:
    count = 0
    rolls = grid.find_all("@")
    for roll in rolls:
        nv = grid.neighbor_values(roll)
        if nv.count("@") < 4:
            count += 1
    return count


def solve_2(grid: Grid) -> int:
    count = 0
    removed = True
    while removed:
        removed = False
        rolls = grid.find_all("@")
        for roll in rolls:
            nv = grid.neighbor_values(roll)
            if nv.count("@") < 4:
                count += 1
                grid[roll] = "."
                removed = True
    return count


grid = Grid(file_content)
print(solve_1(grid))
print(solve_2(grid))
