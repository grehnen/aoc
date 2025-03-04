import os
from utils import fetch_input

current_day = int("".join(filter(str.isdigit, os.path.basename(__file__))))

file_content = fetch_input(current_day)

count = 0
for line in file_content:
    dampening = True
    num_line = list(map(int, line.split()))
    prev = num_line[0]
    increasing = num_line[0] < num_line[1]
    safe = True
    for num in num_line[1:]:
        if (
            num == prev
            or (increasing and num < prev)
            or (not increasing and num > prev)
        ):
            if dampening:
                dampening = False
                prev = num
                continue
            else:
                safe = False
                break
        if abs(num - prev) > 3:
            if dampening:
                dampening = False
                prev = num
                continue
            else:
                safe = False
                break
        prev = num
    if safe:
        count += 1

print(count)
