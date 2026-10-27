class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
    
    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return False
        else:
            self.parent[roota] = self.parent[rootb]
            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        uf = UnionFind(len(edges))
        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]
        