from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats
import numpy as np

file_content: List[str] = fetch_input(__file__)

examples = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  ",
]


def calc_row(num_str: List[str], op: str) -> int:
    if op == "+":
        return sum(int(x) for x in num_str)
    elif op == "*":
        prod = 1
        for num in num_str:
            prod *= int(num)
        return prod
    return 0


def calc_rows(rows: List[List[str]]) -> int:
    count = 0
    for row in rows:
        count += calc_row(row[:-1], row[-1])

    return count


def solve_1(input) -> int:
    matrix = []
    for line in input:
        matrix.append(line.split())
    nump_array = np.array(matrix)
    transposed: List[List[str]] = nump_array.T.tolist()

    return calc_rows(transposed)


def solve_2(input) -> int:
    count = 0
    last_line = input[-1]
    num_rows_count = len(input) - 1
    current_nums = [""]
    current_op = None
    current_start_index = 0

    for i in range(len(last_line)):
        if last_line[i] in ["+", "*"]:
            if current_op is not None:
                count += calc_row(current_nums, current_op)
                current_nums = [""]
                current_start_index = i
            current_op = last_line[i]
        for j in range(num_rows_count):
            num = input[j][i]
            if num == " ":
                continue
            relative_index = i - current_start_index
            while len(current_nums) <= relative_index:
                current_nums.append("")
            current_nums[relative_index] += input[j][i] if num != " " else ""

    if current_op is not None:
        count += calc_row(current_nums, current_op)

    return count


input = file_content
print(solve_1(input))
print(solve_2(input))
