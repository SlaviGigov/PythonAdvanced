data = input().split()
capacity = int(input())
rack = 1
loaded = 0

for n in range(len(data)):
    current = int(data.pop())
    if loaded + current <= capacity:
        loaded += current
    else:
        rack += 1
        loaded = current

print(rack)
# 100/100