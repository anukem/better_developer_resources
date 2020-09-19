# https://leetcode.com/problems/score-after-flipping-matrix/
def score_after_flipping(matrix):
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            matrix[i] = [x ^ 1 for x in matrix[i]]

    for j in range(1, len(matrix[0])):
        col = [row[j] for row in matrix]
        if col.count(0) > col.count(1):
            for index, row in enumerate(matrix):
                matrix[index][j] = row[j] ^ 1

    return calc_score(matrix)
