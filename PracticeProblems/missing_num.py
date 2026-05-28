# Missing Number

nums = [1, 2, 4, 5]

n = 5

total = n * (n + 1) // 2
sum_nums = sum(nums)

print("Missing:", total - sum_nums)