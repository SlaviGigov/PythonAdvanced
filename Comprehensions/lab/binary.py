def to_binary(number):
    bits = []
    while number:
        bits.append(number % 2)
        number //= 2
    bits = [str(el) for el in bits]
    return "".join(bits[::-1])


x = int(input())
print(to_binary(x))
