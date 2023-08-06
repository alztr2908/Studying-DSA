def minEatingSpeed(piles, h) -> int:
    def rateOfEating(val):
        rate = 0
        for p in piles:
            if val > p:
                rate += 1
            elif val <= p:
                rate += p//val+1
        # print(f'{val} and {rate}: {rate<=h}')
        return rate <= h

    l = 1
    r = max(piles)

    while l <= r:
        m = l+(r-l)//2
        # print(l, r, m)
        if rateOfEating(m):
            r = m - 1
        else:
            l = m + 1

    return l


piles = [3, 6, 7, 11]
h = 8
print(f'{piles}: {minEatingSpeed(piles, h)}')
piles = [30, 11, 23, 4, 20]
h = 6
print(f'{piles}: {minEatingSpeed(piles, h)}')
piles = [30, 11, 23, 4, 20]
h = 5
print(f'{piles}: {minEatingSpeed(piles, h)}')
piles = [312884470]
h = 312884469
print(f'{piles}: {minEatingSpeed(piles, h)}')
piles = [1000000000]
h = 2
print(f'{piles}: {minEatingSpeed(piles, h)}')

"""
define search space
    - since koko cannot eat if current pile < proposed pile per hr,
    h will be always be greater or equal than len(piles)
    - min(search_space) = min(piles)
    - max(search_space) max(piles)
    - search space = {min(piles), ..., max(piles)}
"""
