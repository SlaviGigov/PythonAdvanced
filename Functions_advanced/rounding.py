def absolute_value(*args):
    return [round(float(el)) for el in args]

data = input().split()
print(absolute_value(*data))