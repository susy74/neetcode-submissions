class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res = 0, 0
        for r, price in enumerate(prices):
            if prices[l] > price:
                l = r
            res = max(res, price - prices[l])
        return res