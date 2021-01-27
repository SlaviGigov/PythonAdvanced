def operate(command, *args):
    result = 0
    for num in args:
        if command == "+":
            result += int(num)
        elif command == "-":
            result -= int(num)
    if command == "*":
        result = 1
        for num in args:
            result *= int(num)
    if command == "/":
        result = args[0]
        for n in range(1, len(args)):
            result /= args[n]
    return result

# 80/100