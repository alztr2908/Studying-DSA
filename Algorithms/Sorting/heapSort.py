"""
1. Create max heap
2. Remove largest item
3. Place item in sorted partition
"""


def buildMaxHeap(arr):
    n = len(arr)-1
    for i in range(n//2, -1, -1):
        heapify(arr, i)


def heapify(arr, p):
    left = 2*p+1
    right = 2*p+2

    # print(left)
    # print(right)
    # # print(arr[p])
    # print(len(arr)-1)
    if left <= len(arr)-1 and arr[left] > arr[p]:
        max = left
    else:
        max = p

    if right <= len(arr) - 1 and arr[right] > arr[max]:
        max = right

    # print(max)
    # print(p)
    # print()

    if max != p:
        arr[max], arr[p] = arr[p], arr[max]
        heapify(arr, max)


def heapSort(arr):
    buildMaxHeap(arr)
    print(arr)
    n = len(arr)-1

    while n >= 0:
        arr[n], arr[0] = arr[0], arr[n]
        n -= 1
        heapify(arr[:n], 0)
    print(arr)


arr = [1, 7, 6, 4, 3, 2, 5]
heapSort(arr)
