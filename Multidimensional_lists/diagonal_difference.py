n = int(input())
matrix = [(input().split()) for _ in range(n) ]
left = sum(int(matrix[i][i]) for i in range(n))
right = 0
m = n

for i in range(n):
    right += int(matrix[m-1][i])
    m -= 1

print(abs(right-left))
