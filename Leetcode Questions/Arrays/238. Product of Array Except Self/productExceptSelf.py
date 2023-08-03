"""
Solution 1: using prefix and postfix array and getting their index based on the current index of nums

set prefix products - accumulating array based on past products of elements
array = [1,2,3,4]
prefix = [1,2,6,24]

set postfix products - accumulating array based on past products of elements in reverse order
array = [1,2,3,4]
postfix = [24,24,12,4]

since prefix and postfix are product accumulators we can just get the previous element of target index 
in prefix array and next element of postfix array

example: 
array = [1,2,3,4]
prefix = [1,2,6,24]
postfix = [24,24,12,4]

index of 2: 1
target prefix index: 0
target postfix index: 2

result = prefix[0] * postfix[2] = 1*12 = 12
same result if 1*3*4 = 12

if index is first and last element,
just make the result 1.
"""


# Time complexity: O(n)
# Space complexity: O(n)
# Solution is spacious in space
def productExceptSelf_prefixPostfixArray(nums: list[int]) -> list[int]:
    prefix = []
    postfix = [0]*len(nums)

    # Create prefix
    res = 1
    for num in nums:
        res *= num
        prefix.append(res)

    # Create postfix
    res = 1
    for i in range(len(nums)-1, -1, -1):
        print(res)
        res *= nums[i]
        postfix[i] += res

    res = []
    for target_index in range(len(nums)):
        print(target_index)
        if target_index == 0:
            prefix_val = 1
            postfix_val = postfix[target_index+1]
        elif target_index == len(nums)-1:
            prefix_val = prefix[target_index-1]
            postfix_val = 1
        else:
            prefix_val = prefix[target_index-1]
            postfix_val = postfix[target_index+1]

        result = prefix_val * postfix_val

        res.append(result)

    return res


nums = [1, 2, 3, 4]
print(productExceptSelf_prefixPostfixArray(nums))  # [24,12,8,6]

"""
Solution 2: getting prefix values in result array in first iteration then the accumulate postfix values 
on the second iteration 
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    res = []

    pre = post = 1
    for num in nums:
        res.append(pre)
        pre *= num
    for i in range(len(nums)-1, -1, -1):
        res[i] *= post  # same as appending post value
        post *= nums[i]

    return res


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # [24,12,8,6]
