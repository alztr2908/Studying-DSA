def mysqrt(x: int) -> int:
    def condition(value) -> bool:
        if value*value <= x:
            return False

        return True

    l, r = 0, x  # 8

    while l <= r:
        m = (r-l)//2 + l
        # m = (r+l)//2
        print(l, r, m)
        if condition(m):
            r = m - 1
        else:
            l = m + 1
    return l - 1


num = 25
print(mysqrt(num))

"""
if x = 8
[1,2,3,4,5,6,7,8]
 l     m       r
condition(4) = 16 => 16 > 8
[1,2,3,4]
 l   m r
condition(3) = 9 => 9 > 8
[1,2,3]
 l m r
condition(2) = 4 => 4 < 8 (target)



def binary_search(search_space) -> int:
    def condition(value) -> bool:
        pass

    # could be [0, n], [1, n] etc. Depends on problem
    left, right = min(search_space), max(search_space)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


"""
