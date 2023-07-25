# My own implementation
def isAnagram_me(s: str, t: str) -> bool:
    s_dict = dict()

    for letter in s:
        if letter in s_dict:
            s_dict[letter] += 1
        else:
            s_dict[letter] = 1

    for letter in t:
        if letter in s_dict:
            s_dict[letter] -= 1
            if s_dict[letter] < 0:
                return False
        else:
            return False

    for x in s_dict:
        if s_dict[x] > 0:
            return False

    return True


print(isAnagram_me("anagram", "naagram"))
print(isAnagram_me("car", "cat"))
