from typing import List
from utils import fetch_input, Grid, Coord2, Vector2, ints, floats

file_content: List[str] = fetch_input(__file__)

offset = 6 * 0


a: int = ints(file_content[offset + 0])[0]
b: int = ints(file_content[offset + 1])[0]
c: int = ints(file_content[offset + 2])[0]

i = 0
j = 0


instructions = ints(file_content[offset + 4])
output = []


def call_function(opcode, l_operand, part_2=False):
    global a, b, c, i, instructions
    if l_operand <= 3:
        c_operand = l_operand
    else:
        match l_operand:
            case 4:
                c_operand = a
            case 5:
                c_operand = b
            case 6:
                c_operand = c
            case _:
                raise ValueError("Invalid operand")

    assert c_operand is not None
    match opcode:
        case 0:
            a = int(a / 2**c_operand)
        case 1:
            b ^= l_operand
        case 2:
            b = c_operand % 8
        case 3:
            if a != 0:
                i = l_operand - 2
        case 4:
            b ^= c
        case 5:
            out_num = c_operand % 8
            if part_2 and out_num != instructions[len(output)]:
                return False
            output.append(out_num)
            if len(output) > 6:
                print(f"j: 0x{j:x}\nj: {bin(j)} \noutput: {output}")
        case 6:
            b = int(a / 2**c_operand)
        case 7:
            c = int(a / 2**c_operand)
    i += 2
    return True


while i < len(instructions):
    opcode = instructions[i]
    l_operand = instructions[i + 1]
    call_function(opcode, l_operand)

answer_a = ",".join(map(str, output))
print(f"Part 1: {answer_a}")

# Part 2
a: int = ints(file_content[offset + 0])[0]
b: int = ints(file_content[offset + 1])[0]
c: int = ints(file_content[offset + 2])[0]

while True:
    output = []
    a = j
    i = 0
    valid = True
    while i < len(instructions) and len(output) <= len(instructions) and valid:
        opcode = instructions[i]
        l_operand = instructions[i + 1]
        valid = call_function(opcode, l_operand, True)

    if valid and output == instructions:
        print(valid, output, instructions)
        break
    if j % 1000000 == 0:
        print(j)
    j += 1

answer_b = j
print(f"Part 2: {answer_b}")


# (2, 4) | b = a % 8
# (1, 5) | b ^= 5
# (7, 5) | c = a/2^b
# (1, 6) | b ^= 6
# (0, 3) | a = a/8
# (4, 0) | b ^= c
# (5, 5) | print(b % 8)
# (3, 0) | loop
