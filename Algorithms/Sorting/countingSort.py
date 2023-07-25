"""
Pseudocode based on my understanding
- find max element of array
- counting number of occurences in the number of array
- changing occurences from left to right accumulatively
- storing that accumulate from right to left but index-1
- traverse the array and check the equivalent of the values its future indices 
"""

"""
Time complexity: O(n+k) where k is len(arr)
Space complexity: O(n+k) 

Important Notes:
- Counting sort makes assumptions about the data, for example, 
it assumes that values are going to be in the range of 0 to 10 or 10 – 99, etc, 
Some other assumption counting sort makes is input data will be positive integers.

- Like other algorithms this sorting algorithm is not a comparison-based algorithm, 
it hashes the value in a temporary count array and uses them for sorting.

- Counting sort is efficient if the range of input data is not significantly greater 
than the number of objects to be sorted. Consider the situation where the input sequence 
is between the range 1 to 10K and the data is 10, 5, 10K, 5K. 

- Counting sort uses partial hashing to count the occurrence of the data object in O(1).
"""


def countingSort(arr):
    n = len(arr)
    # O(n)
    count_occurences = [0]*(max(arr)+1)
    sorted_arr = [0]*n
    for num in arr:
        count_occurences[num] += 1

    # accumulate occurences from left to right
    for i in range(1, len(count_occurences)):
        count_occurences[i] += count_occurences[i-1]

    # distribute indices from count_occurences[index+1]
    for i in range(len(count_occurences)-1, -1, -1):
        count_occurences[i] = count_occurences[i-1]

        if i == 0:
            count_occurences[i] = 0

    # count occurences has now become the starting index of each element, traverse arr
    # and place it on a new array to be sorted, increment count_occurences[num] by 1
    # every time it has a match in arr
    for i in range(len(arr)):
        index = count_occurences[arr[i]]
        sorted_arr[index] = arr[i]
        count_occurences[arr[i]] += 1

    return sorted_arr


arr = [1, 0, 3, 1, 3, 1]
print(countingSort(arr))
