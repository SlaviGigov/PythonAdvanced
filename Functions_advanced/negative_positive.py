data = [int(el) for el in input().split()]
negatives = sum([el for el in data if el < 0])
positives = sum([el for el in data if el > 0])

print(negatives)
print(positives)

if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")