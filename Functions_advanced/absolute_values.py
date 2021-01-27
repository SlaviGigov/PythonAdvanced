def absolute_value(*args):
    return [abs(float(el)) for el in args]

data = input().split()
print(absolute_value(*data))