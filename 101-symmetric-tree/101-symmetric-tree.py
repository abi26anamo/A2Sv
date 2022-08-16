# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None
        return self.ismirror(root.left,root.right)
    def ismirror(self,left,right):
        if left and right:
             return left.val == right.val and self.ismirror(left.left,right.right) and self.ismirror(left.right,right.left)
        return left == right
        