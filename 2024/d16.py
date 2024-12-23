import os
from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats
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

DIRECTIONS = Vector.all_directions(False)
STEP = 1
TURN = 1000

start_loc = grid.find("S")
start_dir = Vector(1, 0)
reindeer = (start_loc, start_dir)
finish = grid.find("E")

costs: dict[tuple[Coord, Vector], int] = {(start_loc, start_dir): 0}
visited: set[tuple[Coord, Vector]] = set()


while reindeer[0] != finish:
    for d in DIRECTIONS:
        if grid[reindeer[0] + d] != "#" and (reindeer[0] + d, d) not in visited:
            if d == reindeer[1]:
                costs[(reindeer[0] + d, d)] = (
                    costs[reindeer] + STEP
                    if costs.get((reindeer[0] + d, d)) is None
                    else min(costs[reindeer] + STEP, costs[(reindeer[0] + d, d)])
                )
            else:
                costs[(reindeer[0] + d, d)] = (
                    costs[reindeer] + STEP + TURN
                    if costs.get((reindeer[0] + d, d)) is None
                    else min(costs[reindeer] + STEP + TURN, costs[(reindeer[0] + d, d)])
                )
    del costs[reindeer]
    reindeer = min(costs, key=lambda coord: costs[coord])
    if reindeer[0] == finish:
        print(costs[reindeer])
    visited.add(reindeer)
