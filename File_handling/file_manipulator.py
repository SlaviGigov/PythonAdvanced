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
            with open(operation[1], "a") as file:
                file.write(f"{operation[2]}\n")
        except FileNotFoundError:
            print("An error occurred")
    elif operation[0] == "Delete":
        os.remove(command[1])

    command = input()

# the command with REPLACE is not OK