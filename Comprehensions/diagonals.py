matrix = [input().split(", ") for _ in range(int(input()))]
first = [int(matrix[n][n]) for n in range(len(matrix))]
second = [int(matrix[abs(n+1-len(matrix))][n]) for n in range(len(matrix)-1, -1, -1)]
print(f"First diagonal: {', '.join([str(el) for el in first])}. Sum: {sum(first)}")
print(f"Second diagonal: {', '.join([str(el) for el in second])}. Sum: {sum(second)}")
# 100/100