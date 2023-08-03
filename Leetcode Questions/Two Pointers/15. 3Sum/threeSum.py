"""
[-1,0,1,2,-1,-4]
  |        |  |
p1 = -1
p2 = -4
res = curr + temp
if abs(res) == abs(curr) and (curr != p1 or curr != p2):
    append(curr,p1,p2)

case 1: same magnitude but different direction + zero = 0
    [1,-1,0] = 0
    [-2,2,0] = 0
case 2: same magnitude and same direction + same magnitude of two num but different direction = 0
    [1,1,-2] = 0
    [-1,-1,2] = 0
case 3: two elements equate to -3 + 3
    [-5,2,3]
case 4 two elements equate to 3 + -3
    [5,-2,-3]
"""


def threeSum_meSolution(nums):
    # store element with same magnitude either same direction or not.
    # if there is no same magnitude, equate it to -inf
    twoSum = dict()
    # Handles zero edge-case since i can't think of any solution
    numFreq = {0: 0}
    for num in nums:
        if num == 0:
            numFreq[num] += 1
        if num in twoSum:
            twoSum[num].append(num)
        elif -num in twoSum:
            twoSum[-num].append(num)
        else:
            twoSum[num] = []
        if -(num + 3) in twoSum:
            twoSum[-(num + 3)].append(num)
        elif -(num - 3) in twoSum:
            twoSum[-(num - 3)].append(num)

    print(twoSum)
    ans_container = []
    # If value is not -inf, then traverse to nums to find 0 or same magnitude
    for key, value in twoSum.items():
        if len(value) == 0:
            continue
        for val in value:
            for num in nums:
                ans = [key, val, num]
                ans.sort()
                if key == 0 and val == 0 and numFreq[0] < 3:
                    continue
                if sum(ans) == 0 and ans not in ans_container:
                    ans_container.append(ans)
    ans_container.sort()
    return ans_container


nums = [-1, 0, 1, 2, -1, -4]
nums = [-1, 0, 1]
nums = [5, -2, -3]
nums = [5, -2, -3, 7, -4]
nums = [3, 0, -2, -1, 1, 2]
nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
# print(nums)
# print(threeSum_meSolution(nums))


"""
Solution 2: Neetcode solution

example:
[-1,0,1,2,-1,-4]

Sort the array:
[-4,-1,-1,0,1,2]

Loop thru negatives assign a left and right pointer
that slides with the following condition
if less than 0: left++
if greater than 0: right--

if at the start of array the sum is already greater than zero, then early return

"""


def threeSum(nums: list[int]) -> list[int]:
    nums.sort()
    # print(nums)

    three_container = []
    for i in range(len(nums)-2):
        # to avoid repition on previous elements
        if i > 0 and nums[i-1] == nums[i]:
            continue

        left = i+1
        right = len(nums)-1
        while left < right:
            res = [nums[i], nums[left], nums[right]]
            # print(i, res)

            if sum(res) < 0:
                left += 1
            elif sum(res) > 0:
                right -= 1
            else:
                # if res not in three_container:
                three_container.append(res)
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                right -= 1

    return three_container


nums = [-1, 0, 1]
nums = [5, -2, -3]
nums = [5, -2, -3, 7, -4]
nums = [3, 0, -2, -1, 1, 2]
nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
