numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except (ValueError, TypeError):
        print("The variable must be integer")
    except (KeyError, Exception):
        print("Invalid operation")
    line = input()

line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("The number does not exist in the dictionary")
    line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("The number does not exist in the dictionary")
    line = input()

print(numbers_dictionary)
