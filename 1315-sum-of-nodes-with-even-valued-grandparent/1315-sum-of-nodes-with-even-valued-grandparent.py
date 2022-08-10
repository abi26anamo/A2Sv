# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans =0
        def dfs(grandparent,parent,root):
            if not root:
                return
            if grandparent and grandparent.val%2==0:
                self.ans+=root.val
            dfs(parent,root,root.left)
            dfs(parent,root,root.right)
        dfs(None,None,root)
        return self.ans
                
        