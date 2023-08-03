def isPalindrome_me(s: str) -> bool:
    """
    Setup 
    """
    # Step 1: Remove punctuation and spaces
    s = "".join(char for char in s if char.isalnum())

    # Step 2: Convert the string to lowercase
    s = s.lower()

    """
    Main logic for code that uses two pointers
    """
    p1 = 0
    p2 = len(s)-1

    while p2 > p1:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True

# Slower in time complexity since it is somehow
# O(n^2) if there is a lot of non-alphanumeric in string
# Faster in space complexity


def isPalindrome_leetcode(s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
