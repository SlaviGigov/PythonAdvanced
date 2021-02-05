import os

command = input()

while not command == "End":
    operation = command.split("-")
    if operation[0] == "Create":
        open(operation[1], "w")
    elif operation[0] == "Add":
        with open(operation[1], "a") as file:
            file.write(f"{operation[2]}\n")
    elif operation[0] == "Replace":
        try:
            with open(operation[1], "r+") as file:
                text = "".join(file.readlines())
                replaced_content = text.replace(operation[2], operation[3])
                file.seek(0)
                file.write(replaced_content)
        except FileNotFoundError:
            print("An error occurred")
    elif operation[0] == "Delete":
        os.remove(operation[1])

    command = input()

