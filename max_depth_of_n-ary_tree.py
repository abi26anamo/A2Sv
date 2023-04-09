"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
            max_height =0
            for child in node.children:
                child_height = dfs(child)
                max_height = max(max_height,child_height)
            return max_height+1
        return dfs(root)
       






       
