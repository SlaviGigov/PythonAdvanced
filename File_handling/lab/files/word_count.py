import re


def write_result(res):
    with open("output.txt", "w") as file:
        file.writelines("\n".join(res))


def get_file_content(path_to_file):
    with open(path_to_file, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())


result = {}
path_to_words = "words.txt"
path_to_text = "input.txt"

first_file_words = get_file_content(path_to_words)
second_file_words = get_file_content(path_to_text)

for word in first_file_words:
    if word in second_file_words:
        result[word] = second_file_words.count(word)

final_result = [f"{el[0]} - {el[1]}" for el in sorted(result.items(), key=lambda x: -x[1])]
write_result(final_result)

# Nice and difficult with open and compare files
