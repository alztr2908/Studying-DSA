"""
Time complexity: O(n)
Space complexity: O(n)

This problem is like two-sum where dictionary is being 
kept to track the other element of the sum.

In this problem a dictionary is being kept too, in this case,
if the key already existed in the dictionary then it will 
return True immediately. If not, then False
"""


def containsDuplicate_me(nums) -> bool:
    duplicates = dict()

    for i in range(len(nums)):
        if nums[i] in duplicates:
            return True
        duplicates[nums[i]] = 0

    return False


"""
Sample 227ms submission in leetcode
I tried this but it's not really 227ms but 500+ ms
"""


def containsDuplicate_leetCode(nums) -> bool:
    dupl = set()

    for num in nums:
        if num in dupl:
            return True

        dupl.add(num)

    return False


nums = [1, 2, 3, 4]
print(containsDuplicate_me(nums))
print(containsDuplicate_leetCode(nums))
