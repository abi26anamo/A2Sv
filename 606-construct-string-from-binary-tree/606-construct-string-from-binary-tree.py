# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node,res):
            if not node:
                return
            
            res.append(f"({node.val}" if res else str(node.val))
            dfs(node.left,res)
            if node.right and not node.left:
                res.append("()")
            dfs(node.right,res)
            res.append(")")
            return res
        tree_to_str = dfs(root,[])
        return "".join(tree_to_str[:-1])
        
        
