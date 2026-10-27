class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        #adj = {i:[]for i in range(n)}
        adj = collections.defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]                
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        h = [(0, 0)]
        visited = set()
        res = 0
        while len(visited) < n:
            dist, pos =heapq.heappop(h)
                        
            if pos in visited:
                continue
            visited.add(pos)
            res += dist
            for d, p in adj[pos]:
                if p not in visited:
                    heapq.heappush(h, (d,p))
        return res
    



