# https://leetcode.com/problems/unique-paths-iii/
def uniquePathsIII(grid):
    zeros = 0
    for row in grid:
        for el in row:
            if el == 0:
                zeros += 1

    start = (0, 0)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                start = (i, j)

    def explore(grid, current, visited=set(), res=0):
        x, y = current
        if x < 0 or y >= len(grid[0]) or y < 0 or x >= len(grid) or current in visited:
            return 0
        elif grid[x][y] == -1:
            return 0
        if grid[x][y] == 2 and len(visited) == zeros + 1:
            return res + 1


        visited.add(current)
        res += explore(grid, (x + 1, y), visited.copy() )
        res += explore(grid, (x - 1, y), visited.copy() )
        res += explore(grid, (x , y+ 1), visited.copy() )
        res += explore(grid, (x , y- 1), visited.copy() )

        return res

    return explore(grid, start)

