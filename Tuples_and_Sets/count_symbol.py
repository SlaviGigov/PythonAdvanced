def print_result(data):
    data = data_arrange(data)
    for el, n in data.items():
        print(f"{el}: {n} time/s")


def data_arrange(data):
    data_arranged = dict(sorted(data.items(), key=lambda x:x[0]))
    return data_arranged


def create_dict(data):
    result = {}
    for el in data:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1
    return result

result = create_dict(input())
print_result(result)

