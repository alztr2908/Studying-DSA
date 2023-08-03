# My implementation
# Time complexity: O(n)
# Space complexity: O(1)
def reverse(x: int) -> int:

    revert = 0
    negative_flag = 0

    if x < 0:
        x *= -1
        negative_flag = 1

    while x > 0:
        # multiply revert by x to increase its place
        # tens ones => hundreds tens ones
        revert_mut = revert * 10

        # get the ones place of x
        x_mod = x % 10

        # Add the newly moved revert and the new ones in
        # revert together
        revert = revert_mut + x_mod

        # Since the ones place in the original is not needed
        # ones can be removed by floor division by 10
        x = x // 10

    if negative_flag:
        revert *= -1

    # edge cases for values exceeding 4 bytes:
    # 4 bytes: -2^31 to 2^31 - 1
    if revert < -(2**31) or revert > (2**31-1):
        return 0

    return revert


print(reverse(1_534_236_469))
