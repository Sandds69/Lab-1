def spy_game(nums):
    nums = list(filter(lambda n: n == 0 or n == 7, nums))
    li = ''.join([str(n) for n in nums])
    return "007" in li

print(spy_game([1, 2, 4, 0, 0, 5, 0, 0]))