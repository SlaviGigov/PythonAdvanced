data = input()
brackets = []

for n in range(len(data)):
    if data[n] == "(":
        brackets.append(n)
    elif data[n] == ")":
        start = brackets.pop()
        print(data[start:n+1])


