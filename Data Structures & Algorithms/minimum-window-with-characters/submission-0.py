class Solution:
    def minWindow(self, s: str, t: str) -> str:
        conT = collections.defaultdict(int)
        winT = collections.defaultdict(int)
        for c in t:
            conT[c] += 1
        have, need = 0, len(conT)
        l = 0
        res, reslen = [-1, -1], float('inf')
        for r in range(len(s)):
            winT[s[r]] += 1
            if s[r] in conT and conT[s[r]] == winT[s[r]]:
                have += 1
            while have == need:
                winT[s[l]] -= 1
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                if s[l] in conT and winT[s[l]] < conT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if reslen != float('inf') else ''
                