def uniqueElements(nums):
    
    uniqueList = []

    for n in nums:
        if (n not in uniqueList):
            uniqueList.append(n)


    return uniqueList

print(uniqueElements([0, 1, 0, 1, 1, 2, 3]))