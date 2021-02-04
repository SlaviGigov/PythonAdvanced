with open("text2.txt", "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n"
               "-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here. It is safer.")


def read_and_extract(path):
    with open(path, "r") as file:
        text = file.readlines()
    return text


def count_chars(data, output):
    for line in data:
        words = 0
        chars = 0
        line = line.strip()
        for i in line:
            if i.isalpha():
                words += 1
            if not i.isalpha() and i != " ":
                chars += 1
        output[line] = [words, chars]
    return output


def add_line_nums(output, result):
    n = 1
    for key, value in output.items():
        result.append(f"Line {n}: {key} ({value[0]})({value[1]})")
        n += 1
    return result


output = {}
result = []

text = read_and_extract("text2.txt")
count_chars(text, output)
add_line_nums(output, result)

with open("output.txt", "w") as file:
    for line in result:
        file.writelines(f"{line}\n")