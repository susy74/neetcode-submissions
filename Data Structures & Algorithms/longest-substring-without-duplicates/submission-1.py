class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnts = collections.defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(s)):
            cnts[s[r]] += 1
            while cnts[s[r]] > 1:
                cnts[s[l]] -= 1
                
                l += 1
            ans = max(ans, r - l + 1)
        return ans
