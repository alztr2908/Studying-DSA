"""
Time complexity: O(m*n)
    - m: length of letters in inputs
    - n: length of array
Space complexity: O(n*26)
"""


def groupAnagrams(strs):
    str_map = {}

    for s in strs:
        # serve as flag and frequency based on the index of the letter
        # english alphabet is strictly 26 letters (a-z)
        count = [0]*26

        # Indexing count array
        for char in s:
            count[ord(char)-ord("a")] += 1

        # Convert count to tuple since dict is not accepting listss
        if tuple(count) in str_map:
            str_map[tuple(count)].append(s)
        else:
            str_map[tuple(count)] = [s]

    # convert dict_values to list
    return list(str_map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# strs = ["eat", "tea"]
print(groupAnagrams(strs))
