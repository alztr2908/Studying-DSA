def insertionSort(nums):
    for i in range(0, len(nums)-1):
        j = i

        while nums[j] > nums[j+1] and j >= 0:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            j -= 1

    print(nums)


nums = [64, 34, 25, 12, 22, 11, 90]
insertionSort(nums)
