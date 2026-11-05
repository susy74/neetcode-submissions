class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        tmp = []
        def dfs(start):
            if sum(tmp) > target: return 
            if sum(tmp) == target: ans.append(tmp.copy())
            for i in range(start, len(nums)):
                tmp.append(nums[i])
                dfs(i)
                tmp.pop()
        dfs(0)
        return ans