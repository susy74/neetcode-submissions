class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.cnts = size
    
    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return 
        else:
            self.parent[rootb] = roota
            self.cnts -= 1
        return roota
            


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        cnt = n
        F = UnionFind(n)
        visited = set()
        for a, b in edges:
            F.union(a, b)

        return F.cnts
