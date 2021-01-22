rows, cols = [int(el) for el in input().split(",")]
matrix = []

for n in range(rows):
    matrix.append(input().split())

for n in range(cols):
    all = 0
    for m in range(rows):
        all += int(matrix[m][n])
    print(all)
