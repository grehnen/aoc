from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats

file_content: List[str] = fetch_input(__file__)


split_index = file_content.index("")
grid = Grid(file_content[:split_index])
moves = "".join(file_content[split_index + 1 :])

directions = {
    "^": Vector2(0, -1),
    "v": Vector2(0, 1),
    "<": Vector2(-1, 0),
    ">": Vector2(1, 0),
}

for move in moves:
    robot = grid.find("@")
    try:
        assert robot is not None
    except AssertionError:
        print(grid)
        break
    direction = directions[move]
    i = 1
    new_pos = robot + direction * i
    while grid[new_pos] == "O":
        i += 1
        new_pos = robot + direction * i
    if grid[new_pos] == ".":
        for j in range(i, 0, -1):
            grid[robot + direction * j] = grid[robot + direction * (j - 1)]
        grid[robot] = "."

sum_a = 0
for o in grid.find_all("O"):
    sum_a += o.x + o.y * 100

print(sum_a)
