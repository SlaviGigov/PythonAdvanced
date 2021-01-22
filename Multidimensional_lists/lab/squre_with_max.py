rows, cols = input().split(", ")
matrix = [[el for el in input().split(", ")] for _ in range(int(rows))]

top = 0
current = 0
a = 0
b = 0

for i in range(0, int(rows)-1):
    for j in range(0, int(cols)-1):
        current += int(matrix[i][j])
        current += int(matrix[i+1][j])
        current += int(matrix[i][j+1])
        current += int(matrix[i+1][j+1])
        if current > top:
            top = current
            a = i
            b = j
        current = 0

print(f"{matrix[a][b]} {matrix[a][b+1]}")
print(f"{matrix[a+1][b]} {matrix[a+1][b+1]}")
print(top)
