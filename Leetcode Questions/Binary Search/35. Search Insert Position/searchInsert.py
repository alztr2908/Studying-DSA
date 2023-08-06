def searchInsert(nums, target) -> int:
    l, r = 0, len(nums)-1

    while l <= r:
        m = (r-l)//2 + l
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m-1
        else:
            l = m + 1

    # If element not in array return left pointer
    return l


nums = [1, 3, 5, 6]
target = 0
print(searchInsert(nums, target))


"""
Approach like a binary search but lets keep track of left or right pointer???
"""
