import os
from typing import List
from utils import fetch_input, Grid

current_day = int("".join(filter(str.isdigit, os.path.basename(__file__))))

file_content: List[str] = fetch_input(current_day)

import re

grid = Grid(file_content)

sumA = grid.get_any_direction_word_count("XMAS")
print(sumA)

pattern = ["M*S", "*A*", "M*S"]
sumB = grid.get_pattern_count(pattern, any_rotation=True)
print(sumB)
