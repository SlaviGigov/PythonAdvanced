matrix = [[el for el in input()] for _ in range(int(input()))]
x = input()
found = False

for i in range(len(matrix)):
    if found:
        break
    for j in range(len(matrix)):
        if matrix[i][j] == x:
            print(f"({i}, {j})")
            found = True
            break

if not found:
    print(f"{x} does not occur in the matrix")
