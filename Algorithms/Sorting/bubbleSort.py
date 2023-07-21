def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    print(nums)


nums = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(nums)
