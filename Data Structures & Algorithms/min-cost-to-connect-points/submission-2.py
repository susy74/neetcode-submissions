class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        D = collections.defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                d = abs(xi - xj) + abs(yi - yj)
                D[i].append((d, j))
                D[j].append((d, i))
        minH = [(0, 0)]
        ans = 0
        visited = set()
        n = len(points)
        while len(visited) < n:
            d, node = heapq.heappop(minH)
            if node in visited: continue
            visited.add(node)
            ans += d
            for dis, neigh in D[node]:
                if neigh not in visited:
                    # visited.add(neigh)
                    heapq.heappush(minH, (dis,neigh))
        return ans

        