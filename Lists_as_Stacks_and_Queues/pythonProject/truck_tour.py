circle = []
fuel = []

for _ in range(int(input())):
    gas, distance = input().split()
    fuel.append(int(gas))
    circle.append(int(distance))

n = 0
start = 0
tank = 0
count = 0

while True:
    tank += fuel[n]
    tank -= circle[n]
    if tank <= 0:
        tank = 0
        count = 0
        start = n+1
    else:
        count += 1
        if count == len(circle):
            print(start)
            break
    n += 1
    if n == len(circle):
        n = 0
# 80/100 Have to optimize


