# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        prev = float('-inf')
        def dfs(node, prev):
            if not node: return
            # nonlocal prev
            nonlocal ans
            if prev <= node.val:
                ans += 1
            prev = max(prev, node.val)
            dfs(node.left, prev)            
            
            dfs(node.right, prev)
        dfs(root, prev)
        return ans
            