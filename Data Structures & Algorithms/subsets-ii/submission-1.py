class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        nums = sorted(nums)
        def dfs(start):
            ans.append(tmp.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                dfs(i + 1)
                tmp.pop()
        dfs(0)
        return ans