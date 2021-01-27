def combination(data, i):
    if i >= len(data):
        print("".join(data))
        return
    combination(data, i+1)
    for n in range(i + 1, len(data)):
        data[i], data[n] = data[n], data[i]
        combination(data, i + 1)
        data[i], data[n] = data[n], data[i]


data = list(input())
combination(data, 0)