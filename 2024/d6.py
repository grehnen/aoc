import os
from typing import List
from utils import fetch_input, Grid, Coord
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

grid = Grid(file_content.copy())

ORIENTATIONS: List[Coord] = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def next_orientation(orientation: Coord) -> Coord:
    return Coord(ORIENTATIONS[(ORIENTATIONS.index(orientation) + 1) % 4])


def move_one_step(
    grid: Grid, current: Coord, orientation: Coord
) -> tuple[Coord, Coord]:
    while True:
        forward_position = current + orientation
        if not grid.is_in_bounds(forward_position) or grid[forward_position] != "#":
            return forward_position, orientation
        orientation = next_orientation(orientation)

start_time = datetime.now()
start_position = grid.find("^")
position = start_position
orientation = ORIENTATIONS[0]

done_steps = set()

while grid.is_in_bounds(position):
    grid[position] = "X"
    new_position, new_orientation = move_one_step(grid, position, orientation)
    done_steps.add(str((position, new_position)))
    position = new_position
    orientation = new_orientation

print(grid.count("X"))
print(f"Part 1: {datetime.now() - start_time}")


# Part 2
start_time = datetime.now()
possible_positions = set()
grid[start_position] = "."

test_positions =  grid.find_all("X")

for test_position in test_positions:
    position = start_position
    orientation = ORIENTATIONS[0]
    done_steps = set()

    test_position = grid.find("X")
    grid[test_position] = "#"
    loop = False
    looper = 0
    while grid.is_in_bounds(position):
        looper += 1
        new_position, new_orientation = move_one_step(grid, position, orientation)
        if str((position, new_position)) in done_steps:
            possible_positions.add(test_position)
            break
        done_steps.add(str((position, new_position)))
        if looper > 10000:
            print(str((position, new_position)))
        position = new_position
        orientation = new_orientation

    grid[test_position] = "."


print(len(possible_positions))
print(f'Part 2: {datetime.now() - start_time}')
