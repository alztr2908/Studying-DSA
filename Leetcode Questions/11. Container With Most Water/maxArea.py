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
        print()

    return max(maxHeights)


print(maxArea_me([1, 8, 6, 2, 5, 4, 8, 3, 7]))
