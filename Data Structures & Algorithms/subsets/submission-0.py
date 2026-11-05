class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        def dfs(start):
            ans.append(tmp.copy())
            for i in range(start,len(nums)):
                tmp.append(nums[i])
                dfs(i + 1)
                tmp.pop()
        dfs(0)
        return ans