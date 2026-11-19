class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for s, t, v in flights:
            graph[s].append((t, v))
        H = [(0, src, 0)]
        ans = 0
        visited = collections.defaultdict(int)
        while H:
            v, node, stops = heapq.heappop(H)
          
            if node == dst: return v
            if node in visited and visited[node] <= stops: continue
            visited[node] = stops
            if stops <= k:
                for neigh, cost in graph[node]:
                
                    heapq.heappush(H, (cost + v, neigh, stops + 1))

        return -1

        