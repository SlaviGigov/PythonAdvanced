from collections import deque

food = int(input())
data = input().split()
orders = [int(el) for el in data]
orders = deque(orders)
print(max(orders))

for _ in range(len(orders)):
    current = orders.popleft()
    if food >= current:
        food -= current
    else:
        orders.appendleft(current)

if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: ", end="")
    for el in orders:
        print(el, end=" ")

# 100/100 check input data in deque and print