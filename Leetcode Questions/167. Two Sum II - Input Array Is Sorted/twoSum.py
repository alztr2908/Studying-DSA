def twoSum(numbers: list[int], target: int) -> list[int]:
    p1 = 0
    p2 = len(numbers)-1

    while p1 < p2:
        if numbers[p1] + numbers[p2] < target:
            p1 += 1
        elif numbers[p1] + numbers[p2] > target:
            p2 -= 1
        else:
            return [p1, p2]

    return False


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))
