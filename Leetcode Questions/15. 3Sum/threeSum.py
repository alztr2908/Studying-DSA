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


def threeSum(nums):
    # store element with same magnitude either same direction or not.
    # if there is no same magnitude, equate it to -inf
    twoSum = dict()
    # Handles zero edge-case since i can't think of any solution
    numFreq = {0: 0}
    for num in nums:
        print(num)
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
                if key == 0 and val == 0 and numFreq[0] < 3:
                    continue
                if key+val+num == 0:
                    ans = [key, val, num]
                    # allows no duplication of elements
                    if ans not in ans_container:
                        ans_container.append(ans)

    return ans_container


nums = [-1, 0, 1, 2, -1, -4]
nums = [-1, 0, 1]
nums = [5, -2, -3]
nums = [5, -2, -3, 7, -4]
nums = [3, 0, -2, -1, 1, 2]

print(threeSum(nums))
