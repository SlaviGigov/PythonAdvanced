def chairs(m, num, data, result):
    result.append(data[m])
    for n in range(m+1, len(data)):
            result.append(data[n])
            if len(result) == num:
                print(result)
    result = []
    m += 1
    if m == num:
        return
    else:
        chairs(m, num, data, result)

m = 0
result = []
data = input().split(", ")
num = int(input())
chairs(m, num, data, result)