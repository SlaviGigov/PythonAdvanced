from functools import reduce


def multiply(*args):
    # result = 1
    # for el in args:
    #     result *= int(el)
    # return result
    return reduce(lambda x, y: x * y, args)


print(multiply(1, 4, 5))
