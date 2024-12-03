import os
from typing import List
from fetch_input import fetch_input

current_day = int("".join(filter(str.isdigit, os.path.basename(__file__))))

file_content: List[str] = fetch_input(current_day)

print(file_content)
