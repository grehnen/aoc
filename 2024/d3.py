from typing import List
from utils import fetch_input
import re

file_content: List[str] = fetch_input(__file__)

sum = 0
do = True
for line in file_content:
    dos = [m.end() for m in re.finditer(r"do\(\)", line)]
    donts = [m.end() for m in re.finditer(r"don't\(\)", line)]
    spans = [m.span() for m in re.finditer(r"mul\(\d{1,3},\d{1,3}\)", line)]
    span_dict = {span[1]: span for span in spans}
    for span in spans:
        prev_dos = [d for d in dos if d < span[1]]
        prev_donts = [d for d in donts if d < span[1]]
        dos = [d for d in dos if d > span[1]]
        donts = [d for d in donts if d > span[1]]

        if prev_dos:
            max_prev_do = max(prev_dos)
        else:
            max_prev_do = None

        if prev_donts:
            max_prev_dont = max(prev_donts)
        else:
            max_prev_dont = None

        if max_prev_do and (not max_prev_dont or max_prev_do > max_prev_dont):
            do = True
        elif max_prev_dont and (not max_prev_do or max_prev_dont > max_prev_do):
            do = False

        if do:
            match = line[span[0] + 4 : span[1] - 1]
            a, b = map(int, match.split(","))
            sum += a * b

print(sum)
