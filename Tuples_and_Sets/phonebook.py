def print_result(name, data):
    if name not in data:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {data[name]}")


def create_phonebook(data, phonebook):
    name, phone = data.split("-")
    phonebook[name] = phone
    return phonebook


phonebook = {}
data = input()

while not data.isdigit():
    create_phonebook(data, phonebook)
    data = input()

for _ in range(int(data)):
    print_result(input(), phonebook)