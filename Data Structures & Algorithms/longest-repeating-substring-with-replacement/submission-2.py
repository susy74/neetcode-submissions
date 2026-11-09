class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnts = collections.defaultdict(int)
        maxf = 0
        ans = 0
        l = 0
        for r in range(len(s)):
            cnts[s[r]] += 1
            maxf = max(cnts[s[r]], maxf)
            if r - l - maxf + 1 > k:
                
                cnts[s[l]] -= 1
                l += 1
                
            ans = max(ans, r - l + 1)
        return ans