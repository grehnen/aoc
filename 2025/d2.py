from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats

file_content: List[str] = fetch_input(__file__)

sum = 0
sum2 = 0

example = [
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
]

line = file_content[0]
ranges = line.split(",")
for ranger in ranges:
    start, stop = ranger.split("-")
    # 1
    for id in range(int(start), int(stop) + 1):
        id_str = str(id)
        length = len(id_str)
        if length % 2 != 0:
            continue
        first_half = id_str[: length // 2]
        second_half = id_str[length // 2 :]
        if first_half == second_half:
            sum += int(id)

    # 2
    for id in range(int(start), int(stop) + 1):
        id_str = str(id)
        parsed = ""
        for digit in id_str:
            parsed += digit
            if len(parsed) > len(id_str) // 2:
                break
            if len(id_str) % len(parsed) != 0:
                continue

            valid = False
            for i in range(len(id_str)):
                if parsed[i % len(parsed)] != id_str[i]:
                    valid = True
                    break
            if not valid:
                sum2 += int(id)
                break

print(sum)
print(sum2)
