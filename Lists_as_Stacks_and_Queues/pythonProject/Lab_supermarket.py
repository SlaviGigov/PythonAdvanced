from collections import deque

queue = deque([])

while True:
    do = input()
    if do == "Paid":
        for _ in range(len(queue)):
            print(queue.popleft())
    elif do == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(do)
