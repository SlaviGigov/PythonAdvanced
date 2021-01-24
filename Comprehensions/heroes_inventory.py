heroes_items = {name: [] for name in input().split(', ')}
heroes_cost = {name: 0 for name in heroes_items}
do = input()

while not do == "End":
    name, item, cost = do.split("-")
    if item not in heroes_items[name]:
        heroes_items[name].append(item)
        heroes_cost[name] += int(cost)
    do = input()

for name, items in heroes_items.items():
    print(f"{name} -> Items: {len(items)}, Cost: {heroes_cost[name]}")

# 100/100 nice job