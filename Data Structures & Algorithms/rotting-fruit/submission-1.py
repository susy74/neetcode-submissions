class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        def dfs(r, c):
            if min(r, c) < 0 or r >= m or c >= n or grid[r][c] == 0 or grid[r][c] == 2 or (r, c) in visited: 
                return
            visited.add((r, c))
            q.append((r, c))
            nonlocal fresh
            fresh -= 1

        step = 0
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            step += 1
        return step if fresh == 0 else -1
