parking = set()

for _ in range(int(input())):
    direction, car = input().split(", ")
    if direction == "IN":
        parking.add(car)
    else:
        parking.remove(car)

if parking:
    for el in parking:
        print(el)
else:
    print("Parking Lot is Empty")

# 50/100