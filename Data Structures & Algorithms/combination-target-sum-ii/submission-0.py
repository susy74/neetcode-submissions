class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, tmp = [], []
        candidates = sorted(candidates)
        
        def bk(start, total):
            if total == target:
                res.append(tmp.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                tmp.append(candidates[i])
                bk(i + 1, total + candidates[i])
                tmp.pop()
        bk(0, 0)
        return res