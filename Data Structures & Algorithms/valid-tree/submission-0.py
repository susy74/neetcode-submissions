class UionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
    
    def find(self, a):
        if a != self.parents[a]:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return False
        self.parents[roota] = rootb
        return True




class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != (len(edges) + 1): return False
        uf = UionFind(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        return True