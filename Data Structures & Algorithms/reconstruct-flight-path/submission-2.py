class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        D = collections.defaultdict(list)
        # tickets = sorted(tickets)
        for t, s in sorted(tickets, reverse = True):
            D[t].append(s)
        ans = []
        def dfs(node):
            while D[node]:
                dfs(D[node].pop())
            

            ans.append(node)
           
        
        dfs('JFK')
        return ans[::-1]

        