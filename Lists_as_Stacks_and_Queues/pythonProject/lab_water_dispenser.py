from collections import deque

queue = deque()
water = int(input())

while True:
    name = input()
    if name == "Start":
        break
    else:
        queue.append(name)

while True:
    do = input()
    if do == "End":
        print(f"{water} liters left")
        break
    elif do[0] == "r":
        do = do.split()
        water += int(do[1])
    else:
        if water >= int(do):
            print(f"{queue.popleft()} got water")
            water -= int(do)
        else:
            print(f"{queue.popleft()} must wait")
