class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(node):
            res = []
            if node:
                res+=traverse(node.left)
                res.append(node.val)
                res+=traverse(node.right)
            return res
        return traverse(root)[k-1]
