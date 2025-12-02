from typing import List
from utils import fetch_input, Grid

file_content: List[str] = fetch_input(__file__)

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
