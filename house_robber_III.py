# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
       memo = {}
       def dp(node):
           if not node:
               return 0
           if node in memo:
               return memo[node]
               
           rob_curr = node.val
           if node.left:
               rob_curr+=dp(node.left.left)+dp(node.left.right)
           if node.right:
               rob_curr+=dp(node.right.left)+dp(node.right.right)

           not_rob_curr = dp(node.left) +dp(node.right)
           memo[node] =  max(rob_curr,not_rob_curr)
           return max(rob_curr,not_rob_curr)
       return dp(root)
        
