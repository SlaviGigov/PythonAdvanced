data = [int(n) for n in input().split(", ")]
positive = [str(n) for n in data if n >= 0]
negative = [str(n) for n in data if n < 0]
even = [str(n) for n in data if n %2 == 0]
odd = [str(n) for n in data if not n%2 == 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

# WRONG PRINTING

