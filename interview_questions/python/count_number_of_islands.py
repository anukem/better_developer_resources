# # Description
# # A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# # Question Statement
# # Example:
# # Given m # 3, n 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# # Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
# # 0 0 0
# # 0 0 0
# # 0 0 0
# # Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# # 1 0 0
# # 0 0 0   Number of islands = 1
# # 0 0 0
# # Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# # 1 1 0
# # 0 0 0   Number of islands = 1
# # 0 0 0
# # Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# # 1 1 0
# # 0 0 1   Number of islands = 2
# # 0 0 0
# # Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# # 1 1 0
# # 0 0 1   Number of islands = 3
# # 0 1 0
# # We return the result as an array: [1, 1, 2, 3]


def dfs(grid, position, visited):
    i, j = position
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or position in visited:
        return 0

    if grid[i][j] == 1:
        visited[position] = 1

        dfs(grid, (i + 1, j), visited)
        dfs(grid, (i - 1, j), visited)
        dfs(grid, (i , j + 1), visited)
        dfs(grid, (i , j - 1), visited)
        return 1
    return 0

def count_islands(grid):
    count = 0
    visited = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += dfs(grid, (i, j), visited)
    return count


def update(grid, position):
    i, j = position
    grid[i][j] = 1
    return grid


def count_num_islands(m, n, positions, grid):
    res = []
    for position in positions:
        grid = update(grid, position)
        res.append(count_islands(grid))

    return res


import pytest

def test_1():
    assert count_num_islands(3, 3, [[0,0], [0,1], [1,2], [1,1]], [[0 for x in range(3)] for y in range(3)]) == [1, 1, 2, 1]

pytest.main()

