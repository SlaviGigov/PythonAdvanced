n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

for row_index in range(n):
    for col in range(n):
        if matrix[row_index][col] == "K":
            
