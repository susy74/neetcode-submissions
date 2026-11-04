# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        prev = 0
        def dfs(node):
            if not node: return
            nonlocal prev
            nonlocal k
            dfs(node.left)
            k -= 1
            if k == 0: prev = node.val
            dfs(node.right)
        dfs(root)
        return prev