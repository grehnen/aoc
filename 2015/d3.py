from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats, Vector3, Coord3

file_content: List[str] = fetch_input(__file__)
directions = file_content[0]


def move(current_loc: Coord2, dir: str) -> Coord2:
    dir_vec = {
        "^": Vector2.UP,
        "v": Vector2.DOWN,
        "<": Vector2.LEFT,
        ">": Vector2.RIGHT,
    }
    return current_loc + dir_vec[dir]


def solve_1(dirs: str):
    location = Coord2(0, 0)
    visited = {location}
    for dir in dirs:
        location = move(location, dir)
        visited.add(location)

    return len(visited)


def solve_2(dirs: str):
    location_s = Coord2(0, 0)
    location_r = Coord2(0, 0)
    visited = {location_s}
    for i, dir in enumerate(dirs):
        if i % 2 == 0:
            location_s = move(location_s, dir)
            visited.add(location_s)
        else:
            location_r = move(location_r, dir)
            visited.add(location_r)

    return len(visited)


print(solve_1(directions))
print(solve_2(directions))
