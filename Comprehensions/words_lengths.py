# data = {name: len(name) for name in input().split(", ")}
# for k, v in data.items():
#     print(f"{k} -> {v}", sep=", ", end="")

data = [f"{name} -> {len(name)}" for name in input().split(", ")]
print(", ".join(data))
# 100/100