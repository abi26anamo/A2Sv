class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        self.res = []
        def bfs(node):
            queue.append(node)
            while queue:
                avg = 0
                curr = len(queue)

                for _ in range(curr):
                    curr_node = queue.popleft()
                    avg+=curr_node.val

                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
                self.res.append(avg/curr)
        bfs(root)
        return self.res
