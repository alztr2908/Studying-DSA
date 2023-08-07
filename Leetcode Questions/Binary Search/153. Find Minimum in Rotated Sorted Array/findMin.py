def findMin(nums) -> int:
    l, r = 0, len(nums)-1

    while l < r:
        m = (r-l)//2+l
        print(nums[l:r+1])
        if nums[m] > nums[r]:
            l = m+1  # right side
        else:
            r = m  # left side

    return nums[l]


nums = [3, 4, 5, 1, 2]
print(findMin(nums))
nums = [6, 7, 0, 1, 2, 3, 4, 5]
print(findMin(nums))
nums = [1, 2, 3, 4, 5]
print(findMin(nums))

"""
[3, 4, 5, 1, 2]
 L     M     R
 [1,2]
 [1]

[6,7,0,1,2,3,4,5]
 L     M       R
 [6,7,0]
 [0]  
if nums[mid] > nums[right]
    search right side
else:
    search left side
"""
