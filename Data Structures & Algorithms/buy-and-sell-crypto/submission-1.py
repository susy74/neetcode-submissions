class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = float('inf')
        ans = 0
        for day, p in enumerate(prices):
            ans = max(ans, p - minval)
            minval = min(minval, p)
        return ans