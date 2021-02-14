class ValueCanNotBeNegativeError(Exception):
    def __init__(self, value):
        super().__init__(f"{n} is not a number")


numbers = [2, "3", -4, -6, 7]

for n in numbers:
    if n < 0:
        raise ValueCanNotBeNegativeError(f"{n} is negative")

print("Still running")