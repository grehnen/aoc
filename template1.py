import os
from fetch_input import fetch_input

current_day = int("".join(filter(str.isdigit, os.path.basename(__file__))))

filename = fetch_input(current_day)

with open(filename, "r") as file:
    pass