with open("text.txt", "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here. It is safer.")


def replace_chars(data):
    chars = ["-", ",", ".", "!", "?"]
    modified_data = []
    for el in data:
        el = el.rstrip()
        for i in el:
            if i in chars:
                el = el.replace(i, "@")
        modified_data.append(el)
    return modified_data


def turned_backwards(data):
    reversed_data = []
    for el in data:
        el = el.split()[::-1]
        reversed_data.append(" ".join(el))
    return reversed_data


def remove_odd_lines(data):
    for n in range(len(data)):
        if not n % 2 == 0:
            data.remove(data[n])
    return data


def print_result(data):
    for el in data:
        print(el)


result = []

with open("text.txt", "r") as file:
    result.append(file.readlines())
    result = [el for el in list(*result)]
    result = remove_odd_lines(result)
    result = replace_chars(result)
    result = turned_backwards(result)
    print_result(result)
