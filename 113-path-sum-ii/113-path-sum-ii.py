# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res =[]
        def dfs(node,path,cursum):
            cursum+=node.val
            sm = path+[node.val]
            if node.left:
                dfs(node.left,sm,cursum)
            if node.right:
                dfs(node.right,sm,cursum)
            if not node.left and not node.right and cursum == targetSum:
                self.res.append(sm)
        if not root:
            return []
        dfs(root,[],0)
        return self.res
                
           
            
        
        
        