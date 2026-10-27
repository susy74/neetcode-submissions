class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, tmp = [], []

        def bk(start):
            if start == len(nums):
                res.append(tmp.copy())
                return
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                bk(start + 1)
                tmp.pop()
        bk(0)
        return res