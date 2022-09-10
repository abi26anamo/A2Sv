# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        def tree2strHelper(root):
            if not root:
                return

            res.append(f"({root.val}" if res else str(root.val))
            tree2strHelper(root.left)
            if root.right and not root.left:
                res.append("()")
            tree2strHelper(root.right)
            res.append(")")

        tree2strHelper(root)
        return "".join(res[:-1])
        