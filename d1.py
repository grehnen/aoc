with open("input.txt", "r") as file:
    right = []
    left = []
    for line in file:
        line = line.strip()
        num1, num2 = map(int, line.split())
        right.append(num1)
        left.append(num2)

right.sort()
left.sort()

sum = 0
for i in range(len(right)):
    sum += abs(right[i] - left[i])

print(sum)

sum2 = 0
for i in range(len(right)):
    sum2 += left[i] * right.count(left[i])

print(sum2)