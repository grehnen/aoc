from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats

file_content: List[str] = fetch_input(__file__)

examples = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]


def solve_row_1(line: str) -> int:
    largest_num = 0
    largest_follower = 0
    for i, num_str in enumerate(line):
        number = int(num_str)
        if number > largest_num and i < len(line) - 1:
            largest_num = number
            largest_follower = 0
        elif number > largest_follower:
            largest_follower = number
    return (largest_num * 10) + largest_follower


def solve_row_2(line: str) -> int:
    nums = [0] * 12
    for i, num_str in enumerate(line):
        frozen = i - (len(line) - 12)
        number = int(num_str)
        for j in range(len(nums)):
            if frozen <= j and nums[j] < number:
                nums[j] = number
                for k in range(j + 1, len(nums)):
                    nums[k] = 0
                break

    assert len(nums) == 12
    string = "".join(str(num) for num in nums)
    return int(string)


sum = 0
sum2 = 0
for line in file_content:
    sum += solve_row_1(line)
    sum2 += solve_row_2(line)

print(sum)
print(sum2)
