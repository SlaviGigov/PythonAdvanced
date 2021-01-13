data = list(input())
result = []

for w in range(len(data)):
    result.append(data.pop())

print("".join(result))