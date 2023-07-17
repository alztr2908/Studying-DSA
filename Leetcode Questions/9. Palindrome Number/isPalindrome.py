# Language-free implementation (my implementation)
# Time complexity = n+n = O(n)
# Space complexity = O(n) because of arrNum and rev_arrNum === SLOW!!!
def isPalindrome_string(x: int) -> bool:
    num_str = str(x)
    arrNum = []
    rev_arrNum = []
    
    for i in num_str:
        arrNum.append(i)
    
    for i in range(len(arrNum)-1,-1,-1):
        rev_arrNum.append(arrNum[i])

    if rev_arrNum == arrNum:
        return True

    return False

def isPalindrome_stringPythonic(x: int) -> bool:
    # make int into array of string
    nums = [i for i in str(x)]
    rev_nums = [i for i in str(x)]
    # reverse the string 
    rev_nums.reverse()
    # check if str == rev_string 
    if nums == rev_nums:
        return True
    
    return False

# Language-free implementation (my implementation)
# not converting to string
def isPalindrome_int(x: int) -> bool:
    if x < 0:
        return False
    nums = []
    inc = 10
    while x > 0:
        rem = x % inc
        nums.append(rem*10//inc)
        x -= rem

        inc *= 10
    
    # Assign two pointers (first and last)
    pointer1 = 0
    pointer2 = len(nums)-1

    while pointer1 < pointer2:
        if nums[pointer1] != nums[pointer2]:
            return False
        
        pointer1 += 1
        pointer2 -= 1
    
    return True

# Leetcode implementation
def isPalindrome(x: int) -> bool:
	# if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
    if x < 0 or (x !=0 and x%10==0):
        return False        
    
    revert = 0
    while x > revert:
        revert = revert * 10 + x % 10
        x = x // 10 

    print(x)
    print(revert//1)

    # if len(x) is even   if len(x) is odd
    return revert == x or x == revert // 10


def main():
    # print(isPalindrome_string(121))
    # print(isPalindrome_string(10))
    # print(isPalindrome_stringPythonic(121))
    # print(isPalindrome_int(1001))
    # print(isPalindrome_int(121))
    # print(isPalindrome_int(10))
    print(isPalindrome(1001))
    print(isPalindrome(121))
    print(isPalindrome(10))

if __name__ == '__main__':
    main()    

    