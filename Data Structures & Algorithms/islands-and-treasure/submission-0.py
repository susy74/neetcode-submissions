class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def addroom(r, c):
            if (min(r, c) < 0 or r == m or c == n or grid[r][c] == -1
            or (r, c) in visited):
                return
            visited.add((r, c))
            q.append((r, c))
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addroom(r + 1, c)
                addroom(r - 1, c)
                addroom(r, c + 1)
                addroom(r, c - 1)
            dist += 1
        

            