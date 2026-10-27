class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        H = set()
        for r in range(len(s)):
            while s[r] in H:
                H.remove(s[l])
                l += 1
            H.add(s[r])
            res = max(res, r - l + 1)
        return res