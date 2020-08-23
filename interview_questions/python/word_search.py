# /* Given a 2D board and a word, find if the word exists in the grid. */
# /*  */
# /* The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. */
# /*  */
# /* Example: */
# /*  */
# /* board = */
# /* [ */
# /*   ['A','B','C','E'], */
# /*   ['S','F','C','S'], */
# /*   ['A','D','E','E'] */
# /* ] */
# /*  */
# /* Given word = "ABCCED", return true. */
# /* Given word = "SEE", return true. */
# /* Given word = "ABCB", return false. */


def validate_path(word, count, point, board, visited):
    i, j = point
    print(i, j)
    if count == len(word):
        return True
    if (
        i < 0
        or j < 0
        or i >= len(board)
        or j >= len(board[i])
        or word[count - 1] != board[i][j]
        or point in visited
    ):
        return False

    visited[point] = True

    if (
        validate_path(word, count + 1, (i + 1, j), board, visited)
        or validate_path(word, count + 1, (i - 1, j), board, visited)
        or validate_path(word, count + 1, (i, j + 1), board, visited)
        or validate_path(word, count + 1, (i, j - 1), board, visited)
    ):
        return True
    else:
        return False


def word_search(word, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if word[0] == board[i][j]:
                found = validate_path(word, 1, (i, j), board, {})
                if found:
                    return True
    return False
