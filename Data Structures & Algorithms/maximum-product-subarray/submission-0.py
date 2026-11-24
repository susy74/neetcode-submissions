class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minv = maxv = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            a = minv * nums[i]
            b = maxv * nums[i]
            maxv = max(nums[i], a, b)
            minv = min(nums[i], a, b)
            ans = max(ans, maxv)
            
        return ans