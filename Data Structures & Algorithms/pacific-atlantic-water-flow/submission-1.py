class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pa = set()
        aa = set()

        m, n = len(heights), len(heights[0])
        ans = []
        def dfs(r, c, visited, prev):
            if min(r, c) < 0 or r >= m or c >= n or heights[r][c] < prev or (r, c) in visited : return
            prev = heights[r][c]
            visited.add((r, c))
            dfs(r + 1, c, visited, prev)
            dfs(r - 1, c, visited, prev)
            dfs(r, c + 1, visited, prev)
            dfs(r, c - 1, visited, prev)
            

        for r in range(m):
            dfs(r, 0 , pa, heights[r][0])
            dfs(r, n - 1, aa, heights[r][-1])
        for c in range(n):
            dfs(0, c, pa, heights[0][c])
            dfs(m - 1, c, aa, heights[m - 1][c])
        for r in range(m):
            for c in range(n):
                if (r, c) in pa and (r, c) in aa:
                    ans.append([r, c])
        return ans
            