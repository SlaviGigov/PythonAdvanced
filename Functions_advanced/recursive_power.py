# def recursive_power(number, power):
#     return int(number) ** int(power)
# 100/100

def recursive_power(number, power):
    if power == 1:
        return number
    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))