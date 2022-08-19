# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []
        curr = [root]
        while curr:
            queue.append(curr)
            curr = []
            for node in queue[-1]:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            val = [[ node.val for node in curr ]for curr in queue]
        return [sum(value)/len(value) for value in val]