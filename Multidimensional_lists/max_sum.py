rows, cols = input().split()
matrix = [input().split() for _ in range(int(rows))]
square_lenght = 3
result = 0
current = 0
a, b = 0, 0

for n in range(int(rows) - 2):
    for m in range(int(cols) - 2):
        for x in range(square_lenght):
            for y in range(square_lenght):
                current += int(matrix[n + y][m + x])
        if current >= result:
            result = current
            a, b = n, m
        current = 0

print(f"Sum = {result}")
print(f"{matrix[a][b]} {matrix[a][b+1]} {matrix[a][b+2]}")
print(f"{matrix[a+1][b]} {matrix[a+1][b+1]} {matrix[a+1][b+2]}")
print(f"{matrix[a+2][b]} {matrix[a+2][b+1]} {matrix[a+2][b+2]}")

# 80/100 the printing could be better