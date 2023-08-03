# My Implementation
# Time complexity: O(n^2)
# Space complexity: O(n)
# Time Limit Exceeded since of O(n^2) implementation
# Think of a better implementation
def maxArea_me(height) -> int:
    maxHeights = []
    for i in range(len(height)):
        max_height = 0
        for j in range(i+1, len(height)):
            ceiling = height[i]
            # print(f'ceiling before: {ceiling}')
            if height[i] > height[j]:
                ceiling = height[j]
            # print(f'ceiling after: {ceiling}')
            if max_height < ceiling*(j-i):
                max_height = ceiling * (j-i)
            # print(f'max_height: {max_height}')
        maxHeights.append(max_height)

    return max(maxHeights)

# Leetcode sample solution
# Time complexity : O(n)
# Space complexity: O(1)
# This implementation uses two pointers strategy to get the maxArea in a linear time
# Since the


def maxArea_leetCode(height) -> int:
    left = 0
    right = len(height) - 1
    maxArea = 0

    while left < right:
        if height[left] > height[right]:
            maxArea = max(maxArea, height[right]*(right-left))
            right -= 1
        elif height[left] < height[right]:
            maxArea = max(maxArea, height[left]*(right-left))
            left += 1
        else:
            maxArea = max(maxArea, height[left]*(right-left))
            right -= 1
            left += 1

    return maxArea


print(maxArea_me([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea_leetCode([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea_leetCode([8, 8, 8]))
