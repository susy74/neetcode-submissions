class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, tmp = [], []
        nums = sorted(nums)
        def bk(start, tmp):
            res.append(tmp.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                bk(i + 1, tmp)
                tmp.pop()
        bk(0, [])
        return res