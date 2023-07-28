"""
Explanation:
    - make frequency its index

    [1,1,2,3]
    [1,1,2]
    [2,3,1]

    [1,1,2,2,3]
    [1,1,1,1,1,1,2,2,2,2,3,3,3,3]
    
    count: [1,2]
    elem:  [3,[1,2]]

    traverse count array with corresponding elements
"""

"""
Time complexity: O(m*n) 
    where 
    m = # of elements inside sub-arrays of element_count
    n = length of num
Space complexity: O(n)
"""


def topKFrequent_linear(nums, k):
    # init count with len(nums)
    # include the 0th count, hence len(nums)+1
    element_count = [[] for _ in range(len(nums)+1)]
    freq_nums = dict()

    # create dictionary with num:frequency
    for num in nums:
        if num in freq_nums:
            freq_nums[num] += 1
        else:
            freq_nums[num] = 1

    # Place num based on its frequency
    # Frequency serves as index of element_count
    for key, val in freq_nums.items():
        element_count[val].append(key)

    k_container = []  # return value
    i = len(element_count)-1

    # start from end since the frequency
    # is now sorted thru its index
    while i >= 0 and k > 0:
        if len(element_count[i]) != 0:
            for elem in element_count[i]:
                # Decrement of k comes first before appending
                # to make sure that 0th k is not appended
                if k >= 1:
                    k -= 1
                else:
                    break  # early return since k = 0

                k_container.append(elem)

        i -= 1

    return k_container


arr1 = [1, 1, 1, 2, 2, 3]
print(topKFrequent_linear(arr1, 2))
