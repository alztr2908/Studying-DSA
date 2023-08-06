def shipWithinDays(weights, days) -> int:
    def feasible(cap):
        ships, currCap = 1, cap
        for w in weights:
            if currCap < w:
                ships += 1
                currCap = cap
            currCap -= w

        return ships <= days

    # Setup search_space for capacities
    left = max(weights)  # lower bound
    right = sum(weights)  # upper bound

    while left < right:
        middle = left+(right-left)//2

        if feasible(middle):
            right = middle
        else:
            left = middle + 1

    return left


weights = [i for i in range(1, 11)]
days = 5
print(shipWithinDays(weights, days))
"""
lower bound - max(weights)
upper bound - sum(weights)

search space = {lower_bound, ... , upper_bound}
proposed_capacity = middle of search space 

check if proposed_capacity satisfies days required
since we need to find minumum, cases like this can happen
search_space = {False,False,True,True,True,True,True}
                 L                M               R
^^^^^^^^^^^^^^^^^^^^ This is why binary search is useful

Since in our search space, a condition was set and some sequential elements 
satifies it while the remaining sequential element does not satisfies it. 
In the case of the search_space above, we want to find  the first element 
that satisfies the condition such that the minimum capacity or the TRUE 
in the search space.

How do we approach this?
Pattern block: 
- setup search_space for capacity and setup binary_search code on that
- the elements in the search space will undergo the condition as the 
  proposed capacity 
- condition check whether the array fits the proposed capacity in required
number of days times 

=========================================================================
generalized binary search code

def condition(val) -> bool:
    pass
    
def binarySearch(search_space):
    l = min(search_space)
    r = max(search_space)

    while l < r:
        m = (r-l)//2 - l

        if condition(m):
            r = m
        else:
            l = m - 1
    
    return l 
"""

"""
weights = [1,2,3,4,5]
search space = 5 to 15
proposed_cap = middle = 10 

1 2 3 4 5
sum = 0 
loop weights:
    if sum 
    sum += weights[el]
"""
