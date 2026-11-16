class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        H = [(grid[0][0], 0, 0)]
        m, n = len(grid), len(grid[0])
        visited = set()
        d = [(1, 0),(0, 1), (-1, 0), (0, -1)]
        while H:
            time, x, y = heapq.heappop(H)
            visited.add((x, y))
            if x == m - 1 and y == n - 1: return time
   
            for dx, dy in d:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:            
                    visited.add((new_x, new_y))
                    heapq.heappush(H, (max(time, grid[new_x][new_y]), new_x, new_y))
                    
      
            
