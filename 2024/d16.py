from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats

file_content: List[str] = fetch_input(__file__)

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
