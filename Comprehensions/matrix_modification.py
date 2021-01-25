n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])

command = input()

while not command == "END":
    do, row, col, value = command.split()
    if not (0 <= int(row) <= n - 1 and 0 <= int(col) <= n - 1):
        print("Invalid coordinates")
    elif do == "Add":
        matrix[int(row)][int(col)] += int(value)
    elif do == "Subtract":
        matrix[int(row)][int(col)] -= int(value)
    command = input()

for line in matrix:
    print(*line)
# 100/100