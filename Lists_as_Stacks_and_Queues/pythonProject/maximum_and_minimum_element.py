from collections import deque

data = deque()

for n in range(int(input())):
    do = input()
    if int(do[0]) == 1:
        _, element = do.split()
        data.append(int(element))
    elif int(do[0]) == 2:
        try:
            data.popleft()
        except:
            pass
    elif int(do[0]) == 3:
        try:
            print(max(data))
        except:
            pass
    elif int(do[0]) == 4:
        try:
            print(min(data))
        except:
            pass

result = []
for a in range(len(data)):
    result.append(str(data.pop()))

print(", ".join(result))

# 80/100 - difficulties with print
