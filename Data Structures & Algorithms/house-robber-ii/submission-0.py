class Solution:
    def rob(self, nums: List[int]) -> int:


        def helper(tmp):
            rb1 = rb2 = 0
            ans = 0
            for t in tmp:
                ans = max(t + rb2, rb1)
                rb2 = rb1
                rb1 = ans
            return ans
        return max(helper(nums[: -1]), helper(nums[1:]), nums[0])
