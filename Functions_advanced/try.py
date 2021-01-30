children = {
    1: "Ema",
    2: "Philip",
}

nums = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x%2 == 0, nums)))
print([el for el in nums if el % 2 == 0])