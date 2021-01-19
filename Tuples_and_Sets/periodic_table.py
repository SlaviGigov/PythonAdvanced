def print_result(data):
    for el in data:
        print(el)


def data_input(times):
    lines = set()
    for _ in range(times):
        for el in input().split():
            lines.add(el)
    return lines


data = data_input(int(input()))
print_result(data)
