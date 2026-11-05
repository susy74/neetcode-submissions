class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        H =[]
        for s in stones:
            heapq.heappush(H,-s)
        while len(H) > 1:
            x = heapq.heappop(H)
            y = heapq.heappop(H)
            if x == y: continue
            heapq.heappush(H, -abs(x - y))
            print(H)
        return -H[0] if H else 0

