reservation_list = set()

for _ in range(int(input())):
    reservation_list.add(input())

guest = input()
while not guest == "END":
    reservation_list.remove(guest)
    guest = input()

vip = []
regular = []
print(len(reservation_list))
for el in reservation_list:
    if el[0].isdigit():
        vip.append(el)
    else:
        regular.append(el)

for guest in sorted(vip):
    print(guest)

for guest in sorted(regular):
    print(guest)
# 100/100