"""
Time complexity: O(n)
Space complexity: O(n)

This problem is like two-sum where dictionary is being 
kept to track the other element of the sum.

In this problem a dictionary is being kept too, in this case,
if the key already existed in the dictionary then it will 
return True immediately. If not, then False
"""


def containsDuplicate(nums) -> bool:
    duplicates = dict()

    for i in range(len(nums)):
        if nums[i] in duplicates:
            return True
        duplicates[nums[i]] = 0

    return False


nums = [1, 2, 3, 4]
print(containsDuplicate(nums))
