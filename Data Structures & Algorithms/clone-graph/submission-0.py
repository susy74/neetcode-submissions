"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        OldtoNew = {}
        def dfs(node):
            if node in OldtoNew:
                return OldtoNew[node]
            copy = Node(node.val)
            OldtoNew[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy
        return dfs(node) if node else None
            
        