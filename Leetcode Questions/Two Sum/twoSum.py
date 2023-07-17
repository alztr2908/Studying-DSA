def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
        """

    """
    Explanation

    - since constraint states that only one solution, array length must be two always 
    - if array length is two then that one solution has been found, we can return it early
    - since the solution is related to each other 

    
    """

    complement = dict()
    
    for i in range(len(nums)):
        res = target - nums[i]
        if res in complement:
            return [complement[res],i]
        complement[nums[i]] = i
    return []