bunker = {key: [] for key in input().split(', ')}
count = 0
quality = []

for _ in range(int(input())):
    group, item, qu = input().split(" - ")
    bunker[group].append(item)
    qu = qu.split(";")
    count += int(qu[0].split(":")[1])
    quality.append(int(qu[1].split(":")[1]))

print(f"Count of items: {count}")
print(f"Average quality: {sum(quality)/(len(bunker)):.2f}")
for k, v in bunker.items():
    print(f"{k} -> {', '.join([str(el) for el in v])}")

# 100/100

