class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node,val):
            if not node:
                return 
            if node.val == val:
                return node
            if node.val >val:
                return search(node.left,val)
            elif node.val < val:
                return search(node.right,val)
            return node
        return search(root,val)
        
