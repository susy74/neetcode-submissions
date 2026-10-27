class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.component = size

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return
        self.parent[roota] = self.parent[rootb]
        self.component -= 1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a,b)
        return uf.component
        