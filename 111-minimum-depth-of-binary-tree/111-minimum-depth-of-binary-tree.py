# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        level =0
        queue = deque([root])
        mindist =sys.maxsize
        while queue:
            level+=1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if curr.left == None and curr.right ==None:
                    mindist = min(mindist,level)
        return mindist