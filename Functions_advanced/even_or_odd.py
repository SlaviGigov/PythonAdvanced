def even_odd(*args):
    if args[-1] == "even":
        return [el for el in args[:-1] if el % 2 == 0]
    else:
        return [el for el in args[:-1] if not el % 2 == 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
