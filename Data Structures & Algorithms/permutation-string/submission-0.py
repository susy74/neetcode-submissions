class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l = 0
        conts = collections.defaultdict(int)
        for c in s1:
            conts[c] += 1
        for r in range(len(s2)):
            conts[s2[r]] -= 1
            while conts[s2[r]] < 0:
                conts[s2[l]] += 1
                l += 1
            if (r - l + 1) == len(s1):
                return True
        return False