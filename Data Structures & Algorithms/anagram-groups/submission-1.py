class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs = sorted(strs)
        H = collections.defaultdict(list)
        for s in strs:
            s1 = (sorted(s))
            H[tuple(s1)].append(s)
        return list(H.values())

