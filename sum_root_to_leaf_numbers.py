# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node,path):
            if not node:
                return
            if not node.left and not node.right:
                path.append(str(node.val))
                self.ans+=int("".join(path))
                return 
            dfs(node.left,path+[str(node.val)])
            dfs(node.right,path+[str(node.val)])
        dfs(root,[])
        return self.ans
        
        
