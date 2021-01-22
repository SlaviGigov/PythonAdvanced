rows, col = input().split(",")
matrix = []
all = 0

for r in range(int(rows)):
    ll = [int(el) for el in input().split(",")]
    all += sum(ll)
    matrix.append(ll)

print(all)
print(matrix)