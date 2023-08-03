def searchMatrix(matrix, target) -> bool:
    n = len(matrix)
    l_o, l_i = 0, 0
    r_o, r_i = n-1, len(matrix[n-1])-1
    m_o = (l_o + r_o)//2
    m_i = (l_i + r_i)//2

    while l_o <= r_o and l_i <= r_i:
        if l_o == r_o and l_i > r_o:
            break

        print("Before")
        print(l_o, l_i)
        print(r_o, r_i)
        print(m_o, m_i)
        print(matrix[m_o][m_i])

        if matrix[m_o][m_i] < target:
            if m_i == len(matrix[m_o])-1:
                l_o = m_o + 1
                l_i = 0
            else:
                l_o = m_o
                l_i = m_i + 1
        elif matrix[m_o][m_i] > target:
            if m_i == 0:
                r_o = m_o - 1
                r_i = len(matrix[r_o])-1
            else:
                r_o = m_o
                r_i = m_i - 1
        else:
            return True

        m_o = (l_o + r_o)//2
        m_i = (l_i + r_i)//2
        print("After")
        print(l_o, l_i)
        print(r_o, r_i)
        print(m_o, m_i)
        print(matrix[m_o][m_i])
        print()
    return False


matrix = [[1]]
matrix = [[1, 1]]
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 7
print(searchMatrix(matrix, target))
"""
0 0     0 0     0 0 
2 3     1 0     0 1 
1 1     0 2     0 0

Need outer index and inner index
need left, right, middle indices
these indices also has outer and inner indices of their own
loop if left > right
mid_outer = (left_outer + right_outer)//2
mid_inner = (left_inner + right_inner)//2
middle = [mid_outer, mid_inner]
"""
