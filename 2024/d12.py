import os
from typing import List
from utils import fetch_input, Grid, Coord, Vector
from datetime import datetime

filename = os.path.basename(__file__)
day = int(
    "".join(filter(str.isdigit, filename)) or datetime.today().day
    if datetime.today().day <= 25
    else 1
)

directory = os.path.basename(os.path.dirname(__file__))
year = int(
    "".join(filter(str.isdigit, directory)) or datetime.today().year
    if datetime.today().month == 12
    else datetime.today().year - 1
)

file_content: List[str] = fetch_input(day, year)

grid = Grid(file_content)
already_visited: set[Coord] = set()


def get_recursive_neighbors(
    coord: Coord, visited: set[Coord], perimeter
) -> tuple[set[Coord], set[Coord], int]:
    visited.add(coord)
    neighbors: set[Coord] = set()
    for neighbor in grid.neighbors(coord, diagonal=False, include_out_of_bounds=True):
        if neighbor in visited:
            continue
        if not grid.is_in_bounds(neighbor) or grid[neighbor] != grid[coord]:
            perimeter += 1
            continue
        neighbors.add(neighbor)
        new_neighbors, visited, perimeter = get_recursive_neighbors(
            neighbor, visited, perimeter
        )
        neighbors.update(new_neighbors)
    return neighbors, visited, perimeter


def get_region(coord: Coord) -> dict:
    region = {"coords": set(), "perimeter": 0}
    region["coords"], visited, region["perimeter"] = get_recursive_neighbors(
        coord, set(), 0
    )
    region["coords"].add(coord)
    already_visited.update(visited)
    return region


regions = []
for i, line in enumerate(grid.grid):
    for j, char in enumerate(line):
        coord = Coord(i, j)
        if coord in already_visited:
            continue
        regions.append(get_region(coord))

sumA = 0
for region in regions:
    sumA += len(region["coords"]) * region["perimeter"]

print(sumA)

def get_side_neghbors(coord: Coord, direction: Vector, region_coords: set[Coord]):
    perp_a = direction.perpendicular()
    perp_b = -direction.perpendicular()
    side_neighbors = set()
    for perp in (perp_a, perp_b):
        i = 1
        while coord + perp * i in region_coords and coord + perp * i + direction not in region_coords:
            side_neighbors.add(coord + perp * i)
            i += 1
    return side_neighbors


def get_region_directional_side_count(region_coords: set[Coord], direction: Vector) -> int:
    side_count = 0
    checked = set()
    for coord in region_coords:
        if coord in checked:
            continue
        checked.add(coord)
        if coord + direction not in region_coords:
            side_count += 1
            checked.update(get_side_neghbors(coord, direction, region_coords))
    return side_count


def get_region_side_count(region_coords: set[Coord]) -> int:
    side_count = 0
    for direction in Vector.all_directions(diagonal=False):
        side_count += get_region_directional_side_count(region_coords, direction)
    return side_count

for region in regions:
    region['side_count'] = get_region_side_count(region["coords"])

sumB = 0
for region in regions:
    sumB += len(region["coords"]) * region["side_count"]


print(sumB)
