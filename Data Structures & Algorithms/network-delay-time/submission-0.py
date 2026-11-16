class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        D = collections.defaultdict(list)
        for s, t, h in times:
            D[s].append((h, t))

        minH = [(0, k)]
        visited = set()
        ans = 0
        while minH:
            time, node = heapq.heappop(minH)
            if node in visited: continue
            visited.add(node)
            ans = time
            for t, s in D[node]:
                if s in visited: continue
                heapq.heappush(minH, (t + ans, s))
        return ans if len(visited) == n else -1



