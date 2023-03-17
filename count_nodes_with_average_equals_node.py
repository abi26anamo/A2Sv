class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def helper(node):
            nonlocal count
            if not node:
                return [0,0]
            l= helper(node.left)
            r = helper(node.right)  
            total = l[0]+r[0]+node.val
            n= l[1]+r[1]+1
            if total//n==node.val:
                count+=1
            return [total,n]
        helper(root)
        return count
