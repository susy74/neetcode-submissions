class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0] = [-prices[0], float('-inf'), 0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
           
            dp[i][1] = dp[i - 1][0] + prices[i]
            # (just sold)
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
            
            # (no stock today, no sell)
        return max(dp[-1][1], dp[-1][2])
