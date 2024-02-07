def has_33(nums):
    li = [str(i) for i in nums]
    li = ''.join(li)
    return "33" in li

print(has_33([1, 2, 3, 5]))