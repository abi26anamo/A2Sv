# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,mx):
            if not node:return 0
            output = 1 if node.val >=mx else 0
            mx = max(mx,node.val)
            output+=dfs(node.left,mx)
            output+=dfs(node.right,mx)
            return output
        return dfs(root,root.val)
        