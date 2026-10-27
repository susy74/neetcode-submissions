class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n  = len(grid), len(grid[0])
        q = deque()
        fresh, time = 0, 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()
                for (dr, dc) in dir:
                    r_new = r + dr
                    c_new = c + dc
                    if (r_new in range(m) and c_new in range(n) and grid[r_new][c_new] == 1):
                        grid[r_new][c_new] = 2
                        q.append((r_new, c_new))
                        fresh -=1
            time +=1
        return time if fresh == 0 else -1


