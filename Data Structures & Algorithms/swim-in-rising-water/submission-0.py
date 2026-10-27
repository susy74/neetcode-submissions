class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dic = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        visited = set()
        hp = [(grid[0][0], 0, 0)]
        m, n = len(grid), len(grid[0])
        while hp:
            time, r, c = heapq.heappop(hp)
            if r == m - 1 and c == n - 1:
                return time
            for dr, dc in dic:
                r_new, c_new = r + dr, c + dc
                if 0 <= r_new < m  and 0 <= c_new < n and (r_new, c_new) not in visited:
                    heapq.heappush(hp,(max(time,grid[r_new][c_new]), r_new, c_new))
                    visited.add((r_new, c_new))