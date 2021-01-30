def combination(data, i):
    if i >= len(data):
        print("".join(data))
        return
    combination(data, i + 1)
    for n in range(i + 1, len(data)):
        data[i], data[n] = data[n], data[i]
        combination(data, i + 1)
        data[i], data[n] = data[n], data[i]


def permute(data, current_index=0):
    if current_index== len(data):
        print("".join(data))
        return
    for i in range(current_index, len(data)):
        data[current_index], data[i] = data[i], data[current_index]
        permute(data, current_index + 1)
        data[current_index], data[i] = data[i], data[current_index]


data = list(input())
permute(data)

