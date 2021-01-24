# result = {int(n) for n in range(int(input()), int(input())+1) for x in range(2,11) if int(n)%x == 0}
# print(list(result))

print([x for x in range(int(input()), (int(input()) + 1)) if any(int(x) % y == 0 for y in range(2, 11))])
# 100/100

# 100/100 BUT with SET than list
