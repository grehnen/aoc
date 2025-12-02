from typing import List
from utils import fetch_input, Grid, ints
from collections import defaultdict
from functools import cmp_to_key

file_content: List[str] = fetch_input(__file__)

rules = defaultdict(lambda: {"before": set(), "after": set()})

for i, line in enumerate(file_content):
    if line == "":
        remainder = file_content[i + 1 :]
        break

    before, after = ints(line)
    rules[before]["after"].add(after)
    rules[after]["before"].add(before)


sumA = 0
remainder_copy = remainder.copy()

for line in remainder:
    numbers = ints(line)
    valid = True
    for i, num in enumerate(numbers):
        postceding = numbers[i + 1 :]
        for num2 in postceding:
            if int(num2) not in rules[num]["after"]:
                valid = False
                break
        if not valid:
            break

    if valid:
        middle_element = numbers[len(numbers) // 2]
        sumA += int(middle_element)
        remainder_copy.remove(line)


print(sumA)

sumB = 0


def compare(a, b):
    if b in rules[a]["after"]:
        return 1
    if a in rules[b]["after"]:
        return -1
    return 0


for line in remainder_copy:
    numbers = ints(line)
    numbers.sort(key=cmp_to_key(compare))
    middle_element = numbers[len(numbers) // 2]
    sumB += middle_element

print(sumB)
