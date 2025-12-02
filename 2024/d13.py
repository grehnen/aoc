from typing import List
from utils import fetch_input, Grid, Coord, Vector, ints, floats
from fractions import Fraction

file_content: List[str] = fetch_input(__file__)

sumA = 0

for i in range(0, len(file_content), 4):
    a = Vector(*ints(file_content[i]))
    b = Vector(*ints(file_content[i + 1]))
    p = Vector(*ints(file_content[i + 2]))

    p_quote = p.x / p.y
    a_quote = a.x / a.y
    b_quote = b.x / b.y

    if (a_quote < p_quote and b_quote < p_quote) or (
        a_quote > p_quote and b_quote > p_quote
    ):
        continue

    a_count = 0
    b_count = 0

    while b_count < 100 and b.x * b_count < p.x and b.y * b_count < p.y:
        b_count += 1

    while a_count < 100 and a.x * a_count < p.x and a.y * a_count < p.y and b_count > 0:
        a_count += 1
        while (
            a.x * a_count + b.x * b_count > p.x or a.y * a_count + b.y * b_count > p.y
        ):
            b_count -= 1
        if (
            a.x * a_count + b.x * b_count == p.x
            and a.y * a_count + b.y * b_count == p.y
        ):
            sumA += a_count * 3 + b_count
            break

print(sumA)

# Brute force didn't work for part 2, so I had to get sofisticated
# Keeping the home built brute force solution for part 1 though, it feels kind of like a piece of art

sumB = 0
for i in range(0, len(file_content), 4):
    a = Vector(*ints(file_content[i]))
    b = Vector(*ints(file_content[i + 1]))
    p = Coord(*ints(file_content[i + 2]))
    p += 10000000000000

    a_k = Fraction(a.y, a.x)
    b_k = Fraction(b.y, b.x)

    a_m = p.y - a_k * p.x
    b_m = 0

    x = (b_m - a_m) / (a_k - b_k)
    y = b_k * x

    b_count = x / b.x
    a_count = (p.x - x) / a.x

    if a_count.is_integer() and b_count.is_integer():
        sumB += a_count * 3 + b_count

print(sumB)
