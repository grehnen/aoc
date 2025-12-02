from typing import List
from utils import fetch_input, Grid
from datetime import datetime

file_content: List[str] = fetch_input(__file__)

grid = Grid(file_content)

trailheads = grid.find_all("0")


def get_path_neighbors(pos, grid):
    if grid[pos] == "9":
        return [pos]
    peaks = []
    neighbors = grid.neighbors(pos, diagonal=False)
    for neighbor in neighbors:
        if int(grid[neighbor]) == int(grid[pos]) + 1:
            peaks += get_path_neighbors(neighbor, grid)
    return peaks


sumA = 0
sumB = 0
start_time = datetime.now()
for th in trailheads:
    v = get_path_neighbors(th, grid)
    sumA += len(set(v))
    sumB += len(v)

print(datetime.now() - start_time)

print(sumA)
print(sumB)
