class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        visited = dict()
        hp = [(0, src, 0)]

        while hp:
            cost, node, stops = heapq.heappop(hp)
            if node == dst:
                return cost
            if node in visited and visited[node] <= stops:
                continue
            visited[node] = stops
            if stops <= k:
                for dest, weight in graph[node]:
                    heapq.heappush(hp, (cost + weight, dest, stops + 1))
        return -1