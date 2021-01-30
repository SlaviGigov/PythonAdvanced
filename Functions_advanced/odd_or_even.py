command = input()
data = [int(el) for el in input().split()]

if command == "Odd":
    print(sum([el for el in data if not el%2 == 0]) * len(data))
else:
    print(sum([el for el in data if el % 2 == 0]) * len(data))