class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        H = []
        for num in nums:
            heapq.heappush(H, -num)
        while k > 0:
            val = heapq.heappop(H)
            k -= 1
        return -val
