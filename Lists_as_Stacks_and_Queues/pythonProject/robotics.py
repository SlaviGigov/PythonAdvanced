from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
robots = []
available_robots = deque()
products = deque()

for el in data:
    name, rtime = el.split("-")
    robot = {}
    robot["name"] = name
    robot["time"] = rtime
    robot["available at"] = time
    robots.append(robot)
    available_robots.append(robot)

product = input()

while not product == "End":
    products.append(product)
    product = input()

time = time + timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot["available at"] = time + timedelta(seconds=int(current_robot["time"]))
        robot = [el for el in robots if el == current_robot][0]
        robot["available at"] = time + timedelta(seconds=int(current_robot["time"]))
        print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r["available at"]:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot["available at"] = time + timedelta(seconds=int(current_robot["time"]))
            robot = [el for el in robots if el == current_robot][0]
            robot["available at"] = time + timedelta(seconds=int(current_robot["time"]))
            print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    time = time + timedelta(seconds=1)





