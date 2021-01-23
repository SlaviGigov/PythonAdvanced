n = int(input())
matrix = [(input().split()) for _ in range(n) ]
left = sum(int(matrix[i][i]) for i in range(n))
right = 0

for i in range(len(matrix)):
    right += int(matrix[n-1][i])
    n -= 1

print(abs(right-left))

# 100/100