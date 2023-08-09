def lengthOfLongestSubstring_me(s: str) -> int:
    curr_sum = 0
    max_sum = 0
    subString = dict()

    for el in s:
        if el not in subString:
            curr_sum += 1
            subString[el] = 0
        else:
            if curr_sum > max_sum:
                max_sum = curr_sum
            curr_sum = 1
            subString = {el: 0}
    print(max_sum, curr_sum)
    return max(max_sum, curr_sum)


def lengthOfLongestSubstring(s: str) -> int:
    max_sum = 0
    subString = dict()
    placeholder_string = []

    for el in s:

        if el not in subString:
            subString[el] = 0
            placeholder_string.append(el)
        else:
            # imitate a do while in python
            flag = True
            while flag:
                # Implement a queue
                subString.pop(placeholder_string[0])
                remove_el = placeholder_string.pop(0)
                if el == remove_el:
                    flag = False

            # print(subString)
            # include the same string in hash and array
            subString[el] = 0
            placeholder_string.append(el)

        if len(placeholder_string) > max_sum:
            max_sum = len(placeholder_string)
        # print(placeholder_string)
    return max_sum


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
s = "bbbbb"
print(lengthOfLongestSubstring(s))
s = "pwwkew"
print(lengthOfLongestSubstring(s))
s = " "
print(lengthOfLongestSubstring(s))
s = "dvdf"
print(lengthOfLongestSubstring(s))

"""

dv = 2
vdf = 3
df = 2
f = 1

O(n^2) solution

dvdf
dv/d -> 2
vd 
vdf -> 3

abcabcbb
abc/a -> 3
bca -> 3
bca/b
cab -> 3
abc -> 3
abc/b -> 3
cb -> 2
b

basically we can just create a "window that tracks the current 
number of elements in the window and if it sees a repeating then we 
just move the window

so in the case of:
abc|abc|bb
...
abc -> 3
cb (should be) -> 2
b -> 1

return highest = 3 # output will be 3

Proposal 
Runtime complexity: O(k*m) where k is the number of elements before duplicate 
that will be remove i.e. "ab"cb -> cb, thus k = 2
"abca" -> ca, thus k = 1
Space complexity: O(n)
"""
