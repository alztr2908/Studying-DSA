# My own implementation 
# Time complexity = O(n)
# Space complexity = O(1) 
def romanToInt_me(s: str) -> int:
    s += '\0'
    romanDict = {"I": 1, "V": 5, "X":10, "L":50, "C":100 ,"D":500 ,"M":1000, "\0": 0}
    flag = 0
    res = 0

    for i in range(len(s)-1):
        if flag == 1:
            flag = 0
            continue

        # Null character was added to make this valid until (len(s)-1)th iteration
        if romanDict[s[i]] < romanDict[s[i+1]]:
            res += romanDict[s[i+1]] - romanDict[s[i]]
            flag = 1 # So it won't add to res at next iteration
        else:
            res += romanDict[s[i]]
         
    return res

def romanToInt_leetcode(s: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number

def romanToInt_leetcodeFastest(s: str) -> int:
    Num = 0
    Roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
        }
    Prev = 0
    for letter in s:
        Next = Roman[letter]
        if Prev >= Next:
            Num += Prev
        else:
            Num -= Prev
        Prev = Next
        print(Num)
    Num += Next

    return Num
# print(romanToInt_me("MCMXCIV"))
# print(romanToInt_me("III"))
# print(romanToInt_me("LVIII"))
# print(romanToInt_leetcode("MCMXCIV"))
# print(romanToInt_leetcode("III"))
# print(romanToInt_leetcode("LVIII"))
print(romanToInt_leetcodeFastest("MCMXCIV"))
print(romanToInt_leetcodeFastest("III"))
print(romanToInt_leetcodeFastest("LVIII"))

"""
s = MCMXCIV
s.append('\0')
res = 0
p1->p2 ... (traverse aside each other)
p1: i
p2: i+1
flag = 0
for i in 0..len(s)-1:
    if flag == 1:
        flag = 0
        continue
    if s[i] < s[i+1]:
        res += s[i+1] - s[i]
        flag = 1
    else:
        res += s[i]


III
123

1. i = 0 
res = 1
2. i = 1 
res = 2
3. i = 2

MCMXCIV
1234567

1. first iteration || i = 0
res = 1000
flag = 0
2. second iteration || i = 1
res = 1900
flag = 1
3. third iteration || i = 2
flag = 0
continue
4. fourth iteration || i = 3
res = 1990
flag = 1
5. fifth iteration || i = 4
flag = 0
continue

"""
"""
Difference between my implementation vs their implementation:

- Hashmap calls uses extra memory, use temp variables
"""
