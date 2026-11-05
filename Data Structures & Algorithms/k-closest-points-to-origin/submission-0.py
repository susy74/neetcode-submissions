class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        H = []
        ans = []
        for x, y in points:

            d = x*x + y*y
            
            heapq.heappush(H, (d, x, y))
        print(H)
        while k > 0:
            d, x, y = heapq.heappop(H)
            k -= 1
            ans.append([x, y])
        return ans