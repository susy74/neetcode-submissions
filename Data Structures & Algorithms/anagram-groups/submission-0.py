class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            Counts = [0] * 26
            for c in s:
                Counts[ord(c) - ord('a')] += 1
            res[tuple(Counts)].append(s)
        return list(res.values())
