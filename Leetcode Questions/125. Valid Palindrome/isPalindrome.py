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


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
