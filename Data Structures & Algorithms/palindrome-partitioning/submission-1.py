class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        def isPali(h):
            l, r = 0, len(h) - 1
            while l <= r:
                if h[l] != h[r]:
                    return False
                l += 1
                r -= 1
            return True
        ans = []
        tmp = []
        def dfs(start):
            if start == len(s):
                ans.append(tmp.copy())
                return
            for i in range(start, len(s)):
                h = s[start: i + 1]
                if isPali(h): 
                    tmp.append(h)
                    dfs(i + 1)
                    tmp.pop()
        dfs(0)
        return ans