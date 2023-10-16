# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            res = []
            if node:
                res+=dfs(node.left)
                res.append(node.val)
                res+=dfs(node.right)
            return res
        curr = dfs(root)
        for i in range(len(curr)-1):
            if curr[i]>=curr[i+1]:
                return False
        return True
