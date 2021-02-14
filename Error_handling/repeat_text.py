def repeat_text(text, count_str):
    return text * int(count_str)

text = "Hello"
count = "2d"

try:
    print(repeat_text(text, count))
except ValueError as err:
    print("Variable times must be an integer")
    print(err)