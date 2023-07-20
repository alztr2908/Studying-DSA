"""
Kadane's algorithm - dynamic programming problem
"""

# Time complexity: O(n^2)
# Space complexity: O(n)


def kadane_naive(nums) -> int:
    max_sum = nums[0]

    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


# Time complexity: O(n)
# Space complexity: O(n)
def kadane_optimized(nums) -> int:
    max_ending_here = 0
    max_so_far = -99999

    for i in range(len(nums)):
        max_ending_here = nums[i] + max_ending_here
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(0, max_ending_here)
        # print(f'nums[{i}]: {nums[i]}')
        # print(f'maxSoFar: {max_so_far}')
        # print(f'maxEndingHere: {max_ending_here}')
        # print()

    return max_so_far


nums = [-2, -3, 4, -1, -2, 1, 5, 3]
print(kadane_naive(nums))
print(kadane_optimized(nums))
