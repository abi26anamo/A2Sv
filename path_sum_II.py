# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.paths = []
        def dfs(node,path,curr_sum):
            curr_sum+=node.val
            curr_path = path+[node.val]

            if node.left:
                dfs(node.left,curr_path,curr_sum)
            if node.right:
                dfs(node.right,curr_path,curr_sum) 
            
            if not node.right and not node.left and curr_sum == targetSum:
                self.paths.append(curr_path)
        if not root:
            return []
        dfs(root,[],0)
        return self.paths 
