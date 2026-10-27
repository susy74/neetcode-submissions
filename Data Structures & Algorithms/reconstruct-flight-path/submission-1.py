class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        map = collections.defaultdict(list)
        for start, dest in sorted(tickets, reverse = True):
            map[start].append(dest)
        res = []
        def dfs(cur):
            while map[cur]:
                dfs(map[cur].pop())
            res.append(cur)
         
        dfs("JFK")
        return res[: : -1]

        




    