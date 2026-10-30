class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, max(nums)
        total = len(nums)
        ans = 0
        while l <= r:
            mid = (r + l) // 2
            cnts = sum(num <= mid for num in nums)
            if cnts > mid:
                r = mid - 1

            else:
                l = mid + 1
        return l
