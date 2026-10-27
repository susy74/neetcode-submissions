class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        def dfs(r, c):
            if (min(r,c) < 0 or r == m or c == n or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            return (dfs(r + 1, c) + dfs(r - 1, c)
            + dfs(r, c + 1) + dfs(r, c - 1)) + 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
