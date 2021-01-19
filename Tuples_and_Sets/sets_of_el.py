def print_result(data):
    for n in data:
        print(n)

n, m = input().split()
a = set()
b = set()

for _ in range(int(n)):
    a.add(input())

for _ in range(int(m)):
    b.add(input())

data = a&b
print_result(data)