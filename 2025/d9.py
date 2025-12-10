from typing import List, Set
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats, Vector3, Coord3
import time

file_content: List[str] = fetch_input(__file__)
example = [
    "7,1",
    "11,1",
    "11,7",
    "9,7",
    "9,5",
    "2,5",
    "2,3",
    "7,3",
]
coords: List[Coord2] = []
for line in file_content:
    coords.append(Coord2(*ints(line)))


def solve_1(coords: List[Coord2]):
    max_size = 0
    for i, coord in enumerate(coords):
        for coord2 in coords[i + 1 :]:
            square_size = (abs(coord.x - coord2.x) + 1) * (abs(coord.y - coord2.y) + 1)
            max_size = max(max_size, square_size)

    return max_size


def solve_2(coords: List[Coord2]):
    max_size = 0
    edge_coords: Set[Coord2] = set()
    for i in range(len(coords)):
        cur_coord = coords[i]
        next_coord = coords[(i + 1) % len(coords)]
        line_coords = cur_coord.get_line_to(next_coord)
        edge_coords.update(line_coords)

    outer_edge_coords = set()
    min_x = min(coord.x for coord in coords)
    min_y_x = min(coord.y for coord in coords if coord.x == min_x)
    start_coord = Coord2(
        min_x - 1, min_y_x
    )  # Start just outside the top-leftmost point
    to_check = [start_coord]
    checked = set()
    while to_check:
        coord = to_check.pop()
        if coord in checked or coord in edge_coords:
            checked.add(coord)
            continue
        checked.add(coord)
        if coord.get_neighbors().intersection(edge_coords):
            outer_edge_coords.add(coord)
            neighbors = coord.get_neighbors(diagonal=False)
            to_check.extend(neighbors.difference(checked))

    for i, coord in enumerate(coords):
        for coord2 in coords[i + 1 :]:
            square_size = (abs(coord.x - coord2.x) + 1) * (abs(coord.y - coord2.y) + 1)
            if square_size < max_size:
                continue

            overlap = False
            for c in outer_edge_coords:
                if c.is_inside_square(coord, coord2, include_border=True):
                    overlap = True
                    break
            if overlap:
                continue

            print("Valid square found:", coord, coord2, "Size:", square_size)
            max_size = square_size

    return max_size


print(solve_1(coords))
print(solve_2(coords))
