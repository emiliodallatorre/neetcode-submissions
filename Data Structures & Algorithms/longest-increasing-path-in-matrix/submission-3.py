class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])

        memo = [[0] * cols for _ in range(rows)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if memo[x][y] != 0:
                return memo[x][y]

            res = 1  
            for dir in directions:
                nx, ny = x + dir[0], y + dir[1]
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                    res = max(res, 1 + dfs(nx, ny))

            memo[x][y] = res
            return res

        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))

        return res