class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        res = nums[0]
        for num in nums:
            total += num
            res = max(res, total)
            if total < 0:
                total = 0
        return res