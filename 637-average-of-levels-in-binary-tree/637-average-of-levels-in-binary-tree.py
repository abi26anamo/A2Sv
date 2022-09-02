# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans =[]
        while queue:
                levelSum = 0
                levelCount = len(queue)
                for _ in range(levelCount):
                    popped = queue.popleft()
                    levelSum+=popped.val
                    if popped.left:
                            queue.append(popped.left)
                    if popped.right:
                            queue.append(popped.right)
                ans.append(levelSum/levelCount)
        return ans
                
        
        
