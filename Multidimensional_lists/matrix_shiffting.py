rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

command = input()

while not command == "END":
    command = command.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        break

    a, b, c, d = int(command[1]), int(command[2]), int(command[3]), int(command[4])
    if a > rows or c > rows or b > cols or d > cols:
        print("Invalid input!")
        break

    command = input()
