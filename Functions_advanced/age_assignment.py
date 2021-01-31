def age_assignment(*args, **kwargs):
    result ={}
    for el in args:
        result[el] = [y for x, y in kwargs.items() if x == el[0]][0]
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
# 100/100