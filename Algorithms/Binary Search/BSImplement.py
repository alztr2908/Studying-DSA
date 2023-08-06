"""
Given a sorted array of {1,2,..,n-1,n}, we can find an 
element in a more efficient way that lessen the range of our
search value each iteration. This is thru binary search

Main idea of binary search is that it will start by having left 
and right pointers: beginning and end indices, respectively. 
We will define the middle element by getting the sum of those indices 
and integer divide it by 2. It will split into 2 subarrays: left and right.  

If middle element is larger than the target element, the array will just be
the left subarray. Otherwise, the right array. The subarray will be narrowed 
until the middle element is the target element. It will stop if left and right 
pointers overlap each other.

The implementation of binary search can be iteratively or recursively, but since 
recursion has O(n) space complexity due to call stack, it is usually done iteratively 
since the space complexity is just O(1). In recursion we really split the array into 
left or right subarray. In iteration, we just limit the pointers to "split" the array

There are two kinds of binary search implementations but it only differs on how 
we split the array
"""


# In the first implementation, the condition of while loop is until
# left pointer is less than or equal than right pointer, but we "split"
# the array by adding/subtracting the middle element by 1.
def binarySearch_first(nums, target) -> bool:
    left = 0
    right = len(nums)-1

    while left <= right:
        middle = (left+right)//2

        if nums[middle] == target:
            return True

        elif nums[middle] > target:
            right = middle - 1

        else:
            left = middle + 1

    return -1


# In the second implementation, the condition of while loop is until
# left pointer is LESS THAN right pointer, but we "split"
# the array by making the right = mid or adding the left pointer by 1
def binarySearch_second(nums, target) -> bool:
    left = 0
    right = len(nums)-1

    while left < right:
        middle = (left+right)//2

        if nums[middle] == target:
            return True

        elif nums[middle] > target:
            right = middle

        else:
            left = middle + 1

    return -1


# In the recursive implementation, the array are being split and will undergo
# another binary search with that certain subarray. Moreover, this implementation
# only focuses on finding if the element is in the search space ONLY.
def binarySearch_recursion(nums, target):
    # Setup pointers
    left = 0
    right = len(nums) - 1
    middle = (left+right)//2

    # If element is not in the array
    if len(nums) == 0:
        return - 1

    # Early return if middle element is the target
    if nums[middle] == target:
        return True

    # Element > target: split into left subarray
    elif nums[middle] > target:
        right = middle - 1
        return binarySearch_recursion(nums[:right+1], target)

    # Element < target: split into right subarray
    else:
        left = middle + 1
        return binarySearch_recursion(nums[left:], target)


# Driver Code
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8
print(binarySearch_first(nums, target))
print(binarySearch_second(nums, target))
print(binarySearch_recursion(nums, target))

"""
However, solving binary search problems are not this kind of easy and requires 
an additional use of patterns in top of the binary search solution pattern. 

Suppose we have a search space. It could be an array, a range, etc. 
Usually it's sorted in ascending order. For most tasks, we can transform 
the requirement into the following generalized form:

Minimize k , s.t. condition(k) is True

The following code is the most generalized binary search template:
"""


def binary_search(search_space) -> int:
    def condition(value) -> bool:
        pass

    # could be [0, n], [1, n] etc. Depends on problem
    left, right = min(search_space), max(search_space)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
