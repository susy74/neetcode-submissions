# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node, layer):
            if not node: return
            nonlocal ans
            if layer == len(ans):
                ans.append(node.val)
            layer += 1
            dfs(node.right, layer)
            dfs(node.left, layer)
        dfs(root, 0)
        return ans