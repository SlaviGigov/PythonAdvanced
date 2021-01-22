rows, cols = input().split()
matrix = [input().split() for _ in range(int(rows))]
result = 0

for n in range(int(rows)-1):
    for m in range(int(cols)-1):
        if matrix[n][m] == matrix[n][m+1] == matrix[n+1][m] == matrix[n+1][m+1]:
            result += 1
print(result)