class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            res = []
            if node:
                res+=traverse(node.left)
                res.append(node.val)
                res+=traverse(node.right)
            return res
        curr = traverse(root)
        for i in range(len(curr)-1):
            if curr[i+1]<=curr[i]:
                return False
        return True
