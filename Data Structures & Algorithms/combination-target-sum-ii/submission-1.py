class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        tmp = []
        candidates = sorted(candidates)
        def dfs(start):
            if sum(tmp) > target: return
            if sum(tmp) == target: ans.append(tmp.copy())
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                tmp.append(candidates[i])
                dfs(i + 1)
                tmp.pop()
        dfs(0)
        return ans