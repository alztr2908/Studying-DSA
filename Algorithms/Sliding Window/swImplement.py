"""
Sliding window algorithm
    - main goal is to reuse the result of one window to
    compute the result of the next window
    - technique for reducing loops being reused
    - In this technique, result of previous step is reuse 
    to compute the result of next step
    - naive approach: nested loops 


Motivation:
    Example: 12 people line up in a non-sorted manner and 
    we will get the max sum of x adjacent people in the line.

        Codify:
            if x = 3
            people = [12,25,30,33,45,61,34,69,72,41,32,43]
            max_sum(people,3) 
        
        Naive approach:
            get first three and loop until the last three 
            elements
            sum([12,25,30])
            sum([25,30,33])
            ...
            sum([41,32,43])

            Runtime complexity: O(3*12) -> O(x*n)

            This is a working implementation but finding 
            the max_sum could be more efficient using 
            "Sliding Window Technique"
        
        Observations for optimization:
            - in the example array above, we can notice that only 
            the first element gets remove as we traverse thru the
            iteration. In the next iteration, next element was
            added
            - 12,"25,30" -> "25,30",33 -> 30,"33,45" -> ...
            - hence the non-removed elements can be preserved 

        Sliding Window:
            - since we have a fixed "window" of elements" in 
            traversing the loop, the window moves per iteration
            - we deal with the "moving window" by subtract what 
            we "left" and "adding" the newly-includes in the 
            window

Basic steps to solve sliding window problems:
    1. Find the size of the window on which 
    the algorithm has to be performed.
    2.  Calculate the result of the first window, 
    as we calculate in the naive approach.
    3. Maintain a pointer on the start position
    4. Run the loop and keep sliding the window by one step
    at a time and slide the pointer one at a time.
    5. Keep track of the results every window

Code implementation below:    
"""


# Time complexity = (n-k+1)*k = nk - k^2 + k = O(n*k)
def max_age_naive(arr, window_length):
    maxAge = 0  # assume no age of zero in group
    for i in range(len(arr)-window_length+1):  # n-k+1
        totalAge = sum(people[i:i+window_length])  # k

        if maxAge < totalAge:
            maxAgeofPeople = people[i:i+window_length]  # 1
            maxAge = totalAge  # 1

    return (maxAge, maxAgeofPeople)


"""
Basically,

sum(arr[n,m]) is equivalent to

sum = 0 
for i in range(n,m+1):
    sum += arr[i]
return sum

O(# of elements)
"""


# Time complexity = k+k+4*(n-k) = 2k+4n-4k = 4n-2k = O(n)
def max_age_SW(arr, window_length):
    totalAge = sum(arr[:window_length])  # k
    maxAge = totalAge  # k

    for i in range(len(arr)-window_length):  # n-k
        totalAge -= arr[i]  # 1
        totalAge += arr[i+window_length]  # 1

        if maxAge < totalAge:
            maxAgeofPeople = people[i+1:i+window_length+1]  # 1
            maxAge = totalAge  # 1

    return (maxAge, maxAgeofPeople)


n = 5
people = [12, 25, 30, 33, 45, 61, 34, 69, 72, 41, 32, 43]
people = [12, 25, 30, 33, 45, 61, 34, 69, 72, 100, 101, 102]
print(max_age_naive(people, n))
print(max_age_SW(people, n))
