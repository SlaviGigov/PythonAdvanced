children = input().split()
hit = int(input())
n = 0

while True:
    stack = []
    if len(children) == 1:
        break
    else:
        for _ in range(hit):
            stack.append(children[n])
            n += 1
            if n > len(children) - 1:
                n = 0
        print(f"Removed {stack[hit-1]}")
        children.remove(stack[hit-1])
        if not n == 0:
            n -= 1

print(f"Last is {children[0]}")
