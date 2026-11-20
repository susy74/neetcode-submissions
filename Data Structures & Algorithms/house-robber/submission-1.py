class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * (n + 1)
        # dp[0] = nums[0]
        # dp[1] = nums[1]
        # for i in range(2, n):
        rb1 = rb2 = ans = 0
        for num in nums:
            # dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            ans = max(num + rb2, rb1)
            rb2 = rb1
            rb1 = ans

        # return dp[n - 1]
        return ans