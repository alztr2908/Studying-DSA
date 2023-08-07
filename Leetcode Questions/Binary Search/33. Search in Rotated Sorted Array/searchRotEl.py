def search(nums, target) -> int:
    l, r = 0, len(nums)-1

    while l <= r:
        m = (r-l)//2+l
        # print(l, m, r)
        # print(nums[l:r+1])
        if nums[m] == target:
            return m
        # Left sub-array
        elif nums[m] >= nums[l]:
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        # Right sub-array
        else:
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 6
print(search(nums, target))
nums = [6, 7, 0, 1, 2, 3, 4, 5]
target = 7
print(search(nums, target))
nums = [5, 1, 3]
target = 3
print(search(nums, target))
"""
[0,1,2]
[0]
it works 

[6, 7, 0, 1, 2, 3, 4, 5]
target = 7

[6,7,0]
it works

[6, 7, 0, 1, 2, 3, 4, 5]
target = 0

[6, 7, 0, 1, 2, 3, 4, 5] -> search right
[2,3,4,5] -> search right
[4,5] -> search right
[5] -> return middle 
not working

EXAMPLE 1:
[4, 5, 6, 7, 0, 1, 2]
 L        M        R
target = 6

[4, 5, 6, 7, 0, 1, 2]
mid = 7, left = 4, target = 6
target in range(4,7): yes then [4,5,6]

[4,5,6]
mid = 5, left = 4, target = 6
target in range(4,5): no then [6]

[6]
mid = 6, left = 6, target = 6
return 6 since mid == target

EXAMPLE 2:
[6, 7, 0, 1, 2, 3, 4, 5]
target = 0

[6, 7, 0, 1, 2, 3, 4, 5]
mid = 1, left = 6, target = 0
target in range(1,6): yes then [6,7,0]

[6,7,0]
mid = 7, left = 6, target = 0
target in range(6,7): no then [0]

[0]
mid = 0, left = 0, target = 0
return 0 since mid == target

EXAMPLE 3:
[1, 2, 3, 4, 5]
target = 5

[1, 2, 3, 4, 5]
mid = 3, left = 1, target = 5
target in range(1,3): no then [4,5]

[4,5]
mid = 4, left = 4, target = 5
target in range(4,4): no then [5]

[5]
mid = 5, left = 5, target = 5
return 5 since mid == target


need to relate middle element to target
while target decides if right and left based on???
1. get middle element
2. compare to num[left]
    if num[mid] is larger:
        if target is in range(num[left],num[mid]):
            right = mid - 1
        else:
            left = mid + 1
    elif num[mid] is smaller:
        if target is in range(num[mid],num[mid]):
            left = mid + 1
        else: 
            right = mid - 1
"""

"""
pseudocode:
 nums[mid] == target: return mid
 nums[mid] > num[left]:
    if target is in range(num[left],num[mid]):
        search left
    else:
        search right
 else:
    if target is in range(num[left],num[mid]):
        search right
    else:
        search left

 return -1 (if element not in search space)
"""
