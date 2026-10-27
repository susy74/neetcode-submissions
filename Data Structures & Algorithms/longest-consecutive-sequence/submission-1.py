class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        cnt = 0
        for num in nums:
            if num - 1 not in nums:
                cnt = 1
                while num + cnt in nums:
                    cnt += 1
                ans = max(ans, cnt)
        return ans
