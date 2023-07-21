def selectionSort(nums):
    for i in range(len(nums)):
        min_value = float('inf')
        min_value_idx = 0
        for j in range(i, len(nums)):
            # Find the smallest element
            if nums[j] < min_value:
                min_value = nums[j]
                min_value_idx = j

        # Swap the current index and min_value_idx
        temp = nums[i]
        nums[i] = nums[min_value_idx]
        nums[min_value_idx] = temp

    print(nums)


nums = [-90, 64, 34, 25, 12, 22, 11]
selectionSort(nums)
