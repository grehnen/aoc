from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats

file_content: List[str] = fetch_input(__file__)

grid = Grid.dots(71, 71)

for i in range(1024):
    coord = Coord(tuple(ints(file_content[i])))
    grid[coord] = "#"


def solve(grid):
    current_location = Coord(0, 0)
    goal = Coord(70, 70)
    directions = Vector.all_directions(diagonal=False)
    locations: dict[Coord, int] = {current_location: 0}
    prev_step: dict[Coord, Coord | None] = {current_location: None}
    visited: set[Coord] = set()

    while current_location != goal:
        for direction in directions:
            new_location = current_location + direction
            if (
                grid.is_in_bounds(new_location)
                and new_location not in visited
                and grid[new_location] != "#"
            ):
                locations[new_location] = locations[current_location] + 1
                prev_step[new_location] = current_location
        visited.add(current_location)
        del locations[current_location]
        if not locations:
            return None
        current_location = min(
            locations,
            key=lambda k: locations[k] + Vector(goal - k).manhattan_distance(),
        )
    path: set[Coord] = set()
    back_track = goal
    while back_track:
        path.add(back_track)
        back_track = prev_step[back_track]
    return path


path_a = solve(grid)
if path_a:
    print(len(path_a))

i = 1024
path_b = path_a or {}
while True:
    coord = Coord(tuple(ints(file_content[i])))
    grid[coord] = "#"
    if coord in path_b:
        path_b = solve(grid)
        if not path_b:
            break
    i += 1


print(grid)
print(Coord(tuple(ints(file_content[i]))))
