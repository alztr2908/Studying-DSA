def binarySearch(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1
    middle = (left+right)//2
    while left <= right:
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:  # if equal then stop the loop immediately
            return middle
        middle = (left+right)//2
    # print(left, right)
    # print(middle)

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(binarySearch(nums, target))

"""
[-1,0,3,5,9,12]
"""
