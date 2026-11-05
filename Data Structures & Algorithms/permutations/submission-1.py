class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        ans = []
        tmp = []
        def dfs():
            if len(tmp) == len(nums):
                ans.append(tmp.copy())
                return
            for i in range(len(nums)):
                if nums[i] in tmp: continue
                tmp.append(nums[i])
                dfs()
                tmp.pop()
        dfs()
        return ans
