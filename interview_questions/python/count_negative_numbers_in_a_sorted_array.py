# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/850047/Python-Solution
#

    def count_negative_numbers(matrix):
    count = 0

    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix[0]) - 1, -1, -1):
            if matrix[i][j] < 0:
                count += 1
            else:
                break

    return count
return count_negative_numbers(grid)
