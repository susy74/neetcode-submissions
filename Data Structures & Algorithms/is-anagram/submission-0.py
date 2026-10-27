class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = collections.defaultdict(int)
        t2 = collections.defaultdict(int)
        for c in s:
            s1[c] += 1
        for c in t:
            t2[c] += 1
        return s1 == t2