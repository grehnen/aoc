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

line = file_content[0]

full_drive_a: List[int | None] = []

for i in range(0, len(line), 2):
    file_size = int(line[i])
    free_size = int(line[i + 1] if i + 1 < len(line) else 0)
    for j in range(file_size):
        full_drive_a.append(i // 2)
    for j in range(free_size):
        full_drive_a.append(None)

full_drive_b = full_drive_a.copy()

first_empty = 0
last_used = len(full_drive_a) - 1
while first_empty < last_used:
    while full_drive_a[first_empty] is not None:
        first_empty += 1
    while full_drive_a[last_used] is None:
        last_used -= 1
    if first_empty < last_used:
        full_drive_a[first_empty], full_drive_a[last_used] = (
            full_drive_a[last_used],
            full_drive_a[first_empty],
        )
        first_empty += 1
        last_used -= 1

end = full_drive_a.index(None)
full_drive_a = full_drive_a[:end]

sumA = 0
for i, file_id in enumerate(full_drive_a):
    sumA += i * file_id

print(sumA)

last_used = len(full_drive_b) - 1
file_id = full_drive_b[last_used]

while last_used > 0:
    moved = False
    while full_drive_b[last_used] is None or full_drive_b[last_used] > file_id:
        last_used -= 1
    file_id = full_drive_b[last_used]
    size = full_drive_b.count(file_id)
    for i, space in enumerate(full_drive_b):
        if (
            space is None
            and i + size < last_used
            and all(x is None for x in full_drive_b[i : i + size])
        ):
            for j in range(size):
                full_drive_b[i + j] = file_id
                full_drive_b[last_used - j] = None
            last_used -= size
            moved = True
            break
    if not moved:
        last_used -= size

sumB = 0
for i, file_id in enumerate(full_drive_b):
    if file_id is not None:
        sumB += i * file_id

print(sumB)
