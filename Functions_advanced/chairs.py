def chairs(num, data):
    m = 1
    for n in range(num):
        print(data[n], data[m])
        m += 1

data = input().split(", ")
num = int(input())
chairs(num, data)