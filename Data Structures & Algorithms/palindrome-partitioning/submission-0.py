class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, tmp = [], []

        def dfs(start):
            if start >= len(s):
                res.append(tmp.copy())
                return
            for i in range(start, len(s)):
                if isPali(start, i, s):
                    tmp.append(s[start : i + 1])   
                    dfs(i + 1)
                    tmp.pop()

        def isPali(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return
                l += 1
                r -= 1
            return True
        
        dfs(0)
        return res


        