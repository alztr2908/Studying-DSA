"""
Pseudocode on my own understanding
- get the frequency of each position of element based on exp 
in count array
- get the actual position by count[index] = count[index-1]
- build output array by getting the index-1 of count array then 
make it an index of output array (basically counting sort)
- put output array into arr 
"""


def countingSort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    # Counting sort but divide by 10 (decimal number system)
    for num in arr:
        index = num // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Build output sort
    # distribute indices from count_occurences[index+1]
    for i in range(len(arr)-1, -1, -1):
        index = arr[i]//exp
        output[count[index % 10]-1] = arr[i]
        count[index % 10] -= 1

    # Copy output to arr for next sorting
    for i in range(len(output)):
        arr[i] = output[i]


def radixSort(arr):
    max_el = max(arr)
    exp = 1

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    while max_el/exp >= 1:
        countingSort(arr, exp)
        exp *= 10

    return arr


arr = [802, 2, 24, 45, 66, 170, 75, 90]
print(radixSort(arr))
