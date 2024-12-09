import os
from typing import List
from utils import fetch_input, Grid
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

antenna_grid = Grid(file_content)
anti_node_grid_a = Grid.dots(antenna_grid.width, antenna_grid.height)
anti_node_grid_b = Grid.dots(antenna_grid.width, antenna_grid.height)

all_chars = antenna_grid.get_char_set(ignore=".")

for char in all_chars:
    antennas = antenna_grid.find_all(char)
    for antenna_1 in antennas:
        for antenna_2 in antennas:
            if antenna_1 == antenna_2:
                continue
            delta = antenna_1 - antenna_2
            if anti_node_grid_a.is_in_bounds(antenna_1 + delta):
                anti_node_grid_a[antenna_1 + delta] = "#"
            i = 0
            while anti_node_grid_b.is_in_bounds(antenna_1 + delta * i):
                anti_node_grid_b[antenna_1 + delta * i] = "#"
                i += 1


print(anti_node_grid_a.count("#"))
print(anti_node_grid_b.count("#"))
