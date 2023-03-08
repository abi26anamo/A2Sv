class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       if not root:
           return []
       queue = deque([root])
       res = []
       while queue:
           n = len(queue)
           curr_level = []
           for _ in range(n):
               curr = queue.popleft()
               if curr.left:
                   queue.append(curr.left)
               if curr.right:
                   queue.append(curr.right)
               curr_level.append(curr.val)
           res.append(curr_level)
       return res
               
