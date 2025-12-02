from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats
from datetime import datetime

file_content: List[str] = fetch_input(__file__)

TIME_SAVE_LIMIT = 100

grid = Grid(file_content)
path = grid.a_star()
path_dict = {coord: i for i, coord in enumerate(path)}
sum_a = 0
for coord in grid.a_star():
    for direction in Vector.all_directions(diagonal=False):
        direction *= 2
        new_location = coord + direction
        if (
            new_location in path_dict
            and path_dict[new_location]
            >= path_dict[coord]
            + TIME_SAVE_LIMIT
            + 2  # + 2 because we are still moving 2 steps while cheating
        ):
            sum_a += 1
print(sum_a)

CHEAT_LIMIT = 20
sum_b = 0
start = datetime.now()
for i, coord_a in enumerate(path):
    for coord_b in path[i + TIME_SAVE_LIMIT :]:
        vector = Vector(coord_b - coord_a)
        if (
            vector.manhattan_distance() <= CHEAT_LIMIT
            and path_dict[coord_b]
            >= path_dict[coord_a] + TIME_SAVE_LIMIT + vector.manhattan_distance()
        ):
            sum_b += 1

print(sum_b)
