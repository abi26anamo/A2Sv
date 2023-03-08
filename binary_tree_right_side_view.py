class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        if not root:
            return 
        res  = []
        while queue:
            n = len(queue)
            curr_element = []
            for _ in range(n):
                curr = queue.popleft()
                curr_element.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr_element[-1])
        return res
