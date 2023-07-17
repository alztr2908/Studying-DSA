# My own implementation 
def romanToInt_me(s: str) -> int:
    s += '\0'
    print(s, end=": ")
    romanDict = {"I": 1, "V": 5, "X":10, "L":50, "C":100 ,"D":500 ,"M":1000, "\0": 0}

    flag = 0
    res = 0

    for i in range(len(s)-1):
        if flag == 1:
            flag = 0
            continue
        # print(res)
        # print(romanDict[s[i]])
        # print(romanDict[s[i+1]])
        # print()
        # Null character was added to make this valid until (len(s)-1)th iteration
        if romanDict[s[i]] < romanDict[s[i+1]]:
            res += romanDict[s[i+1]] - romanDict[s[i]]
            flag = 1 # So it won't add to res at next iteration
        else:
            res += romanDict[s[i]]
         
    return res

print(romanToInt_me("MCMXCIV"))
print(romanToInt_me("III"))
print(romanToInt_me("LVIII"))
# flag = 0
# for i in range(5):
#     if flag == 1:
#         flag = 0
#         continue
#     if i == 1:
#         flag = 1
#     print(i)

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

