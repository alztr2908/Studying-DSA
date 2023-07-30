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
    while i >= 0:
        if len(element_count[i]) != 0:
            for elem in element_count[i]:
                if len(k_container) == k:
                    return k_container  # early return since k is reached

                k_container.append(elem)

        i -= 1

    return k_container


arr1 = [1, 1, 1, 2, 2, 3, 3, 3, 3,]
arr2 = [1]
print(topKFrequent_linear(arr1, 3))
print(topKFrequent_linear(arr2, 1))

"""
Heap Implementation
 - create dictionary (num: frequency)
 - create heap structure (some sort of heapSort)
 - repeat heapSort k times
 - heapify cost: log(n)

 HeapSort:
    1. Create max heap
    2. Remove largest item
    3. Place item in sorted partition

Time complexity: O(k*log(n)) 
"""


def topKFrequent_heap(nums, k):
    freq_nums = dict()
    freq_arr = list()

    """
    get method => dict.get(key,value) 
    Parameter:
        key - key
        value - Optional. A value to return if the specified key does not exist.
                Default value None
    """
    # Get the frequency of each nums
    for num in nums:
        freq_nums[num] = 1 + freq_nums.get(num, 0)

    # Convert dict to (num,frequency) array
    for key, value in freq_nums.items():
        freq_arr.append((value, key))

    # print(freq_arr)
    # Create a max heap structure to get the freq_arr element k times only
    # Sort by value in (value,key) since first element in tuple is the basis of comparison
    buildMaxHeap(freq_arr)

    # print(freq_arr)
    k_container = []
    # Get the root k times
    k_item = len(freq_arr)-1-k
    for i in range(len(freq_arr)-1, k_item, -1):
        freq_arr[i], freq_arr[0] = freq_arr[0], freq_arr[i]
        k_container.append(freq_arr[i][1])
        heapify(freq_arr, i, 0)

    return k_container


# Build max heap structure by heapifying first half
# of the elements since those elements have
# child nodes (usually)
def buildMaxHeap(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)


# Heapify is for maintaining the heap invariant
# Max heap invariant - parent is always greater than child nodes
def heapify(arr, length_arr, p):
    # heap property in array (zero-based)
    left = 2*p+1
    right = 2*p+2
    max = p

    # Check if left child is greater than parent
    if left < length_arr and arr[left] > arr[p]:
        max = left
    # Check if right child is greater than current max
    # Since if left > p => max = left
    if right < length_arr and arr[right] > arr[max]:
        max = right

    # if parents is both greater, no heapify will occur
    if max != p:
        arr[max], arr[p] = arr[p], arr[max]  # swap
        heapify(arr, length_arr, max)


arr1 = [1, 2, 2, 3, 100, 100]
print(topKFrequent_heap(arr1, 1))
