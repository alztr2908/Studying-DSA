def firstBadVersion(n: int) -> int:
    l = 0
    r = n

    while l <= r:
        m = (l+r)//2
        if isBadVersion(m):
            r = m-1
        else:
            l = m+1

    return l


def isBadVersion(n) -> bool:
    if n >= 5:
        return True

    return False
