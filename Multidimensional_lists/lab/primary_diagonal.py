matrix = [(input().split()) for _ in range(int(input())) ]
print(sum(int(matrix[i][i]) for i in range(len(matrix[0]))))