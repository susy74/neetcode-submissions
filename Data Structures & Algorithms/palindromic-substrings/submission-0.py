class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        def isPali(l, r):
            counts = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                counts += 1
            return counts
        
        for i in range(len(s)):
            ans += isPali(i, i)
            ans += isPali(i, i + 1)
        return ans



