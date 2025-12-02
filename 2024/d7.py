from typing import List
from utils import fetch_input, ints

file_content_a: List[str] = fetch_input(__file__)
file_content_b: List[str] = file_content_a.copy()


def f(total, terms, mode) -> List[int]:
    if len(terms) == 2:
        results = [terms[0] + terms[1], terms[0] * terms[1]]
        if mode == "b":
            results.append(int(str(terms[0]) + str(terms[1])))
        return results
    else:
        results = []
        for i in f(total, terms[:-1], mode):
            results.append(terms[-1] + i)
            results.append(terms[-1] * i)
            if mode == "b":
                results.append(int(str(i) + str(terms[-1])))
        results = [i for i in results if i <= total]
        return results


sum_a = 0
sum_b = 0
for line in file_content_a:
    numbers = ints(line)
    total = numbers[0]
    terms = numbers[1:]
    all_results = f(total, terms, "a")
    if total in all_results:
        file_content_b.remove(line)
        sum_a += total
        sum_b += total

print(sum_a)

for i, line in enumerate(file_content_b):
    numbers = ints(line)
    total = numbers[0]
    terms = numbers[1:]
    all_results = f(total, terms, "b")
    if total in all_results:
        sum_b += total

print(sum_b)
