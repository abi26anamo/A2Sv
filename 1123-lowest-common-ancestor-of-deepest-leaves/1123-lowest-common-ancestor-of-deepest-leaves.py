# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getDeepestlevel(node,level):
            nonlocal ans , deepest
            deepest = max(deepest,level)
            if not node:
                return level
            left_level = getDeepestlevel(node.left,level+1)
            right_level = getDeepestlevel(node.right,level+1)
            if left_level == right_level == deepest:
                ans = node
            return max(left_level,right_level)
        deepest =0
        ans =None
        getDeepestlevel(root,0)
        return ans