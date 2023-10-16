# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        prefix_hash = defaultdict(int)
        prefix_hash[0]=1 

        def dfs(node,cumulative):
            if not node:
                return 0
            cumulative+=node.val 
            count = prefix_hash[cumulative-targetSum]
            prefix_hash[cumulative] +=1 

            count+=dfs(node.left,cumulative)
            count+=dfs(node.right,cumulative)
            prefix_hash[cumulative]-=1

            return count
        return dfs(root,0)
