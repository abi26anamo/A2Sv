"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxdepth =0
        for node in root.children:
            maxdepth = max(self.maxDepth(node),maxdepth)
        return 1+maxdepth
        