class UnionFind:
    
    def __init__(self, size):
        self.parent = list(range(size + 1))
        print(self.parent)

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return [a, b]
        self.parent[roota] = rootb
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        F = UnionFind(len(edges))
        res = []
        for a, b in edges:
            res = F.union(a, b)
            if res: return res

        
        