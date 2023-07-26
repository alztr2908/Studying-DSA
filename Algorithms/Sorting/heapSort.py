"""
1. Create max heap
2. Remove largest item
3. Place item in sorted partition
"""

"""
Time Complexity: O(N log N)
Auxiliary Space: O(log n), due to the recursive call stack. However, auxiliary space can be O(1) for iterative implementation.
"""

# Build a heap


def buildMaxHeap(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

# Maintaining heap property thru recursion


def heapify(arr, N, p):
    left = 2*p+1
    right = 2*p+2
    max = p

    if left < N and arr[left] > arr[p]:
        max = left

    if right < N and arr[right] > arr[max]:
        max = right

    if max != p:
        arr[max], arr[p] = arr[p], arr[max]
        heapify(arr, N, max)


def heapSort(arr):
    N = len(arr)
    buildMaxHeap(arr)
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    print(arr)


arr = [1, 7, 6, 4, 3, 2, 5]
arr2 = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print()
heapSort(arr2)
