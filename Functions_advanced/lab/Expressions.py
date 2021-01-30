def expressions(nums, current_sum=0, result = ""):
    if not nums:
        return [(result, current_sum)]

    result_plus = expressions(nums[1:], current_sum + nums[0], f"{result}+{nums[0]}")
    result_minus = expressions(nums[1:], current_sum - nums[0], f"{result}-{nums[0]}")
    return result_plus + result_minus

nums = [int(el) for el in input().split(", ")]
# nums = [1, 1, 1, 1]
print(*[f"{el[0]}={el[1]}" for el in expressions(nums)], sep="\n")