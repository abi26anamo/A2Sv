class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}
        def helper(root,row,col):
            if not root:
                return 
            result[root] = [row,col]
            helper(root.left,row+1,col-1)
            helper(root.right,row+1,col+1)
            return result
        helper(root,0,0)
        colMap = defaultdict(list)
        for key in result.keys():
            colMap[result[key][1]].append(key)

        for col in colMap.keys():
            colMap[col] = sorted(colMap[col],key = lambda x:(result[x][0],x.val))

        vertical_nodes =[]
        for col in sorted(colMap.keys()):
            curr = []
            for node in colMap[col]:
                curr.append(node.val)
            vertical_nodes.append(curr)
        return vertical_nodes
