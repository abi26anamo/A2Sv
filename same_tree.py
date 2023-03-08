class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        else:
            left = self.isSameTree(p.left,q.left)
            right = self.isSameTree(p.right,q.right)
            if left and right:
                return p.val==q.val
