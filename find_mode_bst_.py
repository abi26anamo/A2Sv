class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(node):
            res = []
            if node:
                res+=traverse(node.left)
                res.append(node.val)
                res+=traverse(node.right)
            return res

        nodes = traverse(root)
        count = Counter(nodes)
        new_dict = defaultdict(list)
        
        for c,val in count.items():
            new_dict[val].append(c)

        return new_dict[sorted(new_dict.keys())[-1]]
            
