"""
left and right pointer at start and end of array, respectively
max_area = 0
height = min(num[left],num[right])
width = left - right
current_area = height*width
max_area = max(current_area,max_area)
iterate while l < r

array traversal:
since this is greedy algo(max area is target),
we can traverse if the element in left is greater than right 
then right-- to find larger element, otherwise right++, 
if equal then move left and right
"""


def maxArea(height) -> int:
    max_area = 0
    l, r = 0, len(height)-1

    while l < r:
        h = min(height[l], height[r])
        w = r - l
        current_area = h*w
        max_area = max(current_area, max_area)

        # traversal
        if height[l] > height[r]:
            r -= 1
        elif height[l] < height[r]:
            l += 1
        else:
            l += 1
            r -= 1

    return max_area


nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
nums = [8, 8, 8]
print(maxArea(nums))
