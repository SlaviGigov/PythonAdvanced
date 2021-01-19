# data = input().split()
# unique_data = set(data)
#
# for el in unique_data:
#     print(f"{float(el)} - {data.count(el)} times")
#
# 100/100

data = input().split()
result = []

for el in data:
    if el not in result:
        print(f"{float(el)} - {data.count(el)} times")
        result.append(el)