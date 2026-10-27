class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        conts = collections.defaultdict(int)
        l , res = 0, 0
        maxf = 0
        for r in range(len(s)):
            conts[s[r]] += 1
            maxf = max(maxf, conts[s[r]])
            if (r - l + 1) - maxf > k:
                conts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res