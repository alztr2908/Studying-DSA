"""
1. Create max heap
2. Remove largest item
3. Place item in sorted partition
"""


def buildMaxHeap(arr):
    n = len(arr)-1
    for i in range(n//2, -1, -1):
        heapify(arr, i)
        # print(arr)


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

    if right <= len(arr) - 1 and arr[right] > arr[p]:
        max = right

    print(max)
    print(p)
    print()

    if max != p:
        print("hello")
        print(arr)

        print(arr)
        heapify(arr, max)


def heapSort(arr):
    buildMaxHeap(arr)
    print(arr)


arr = [1, 7, 6, 4, 3, 2, 5]
heapSort(arr)
