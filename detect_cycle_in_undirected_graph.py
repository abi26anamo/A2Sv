from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		n = len(adj)
		colors =[0 for _ in range(n)]
		self.count = 0
		def dfs(node,parent):
            if colors[node]==1:
                return True
            colors[node]=1

            for neighbor in adj[node]:
                if colors[neighbor]==2:
                    continue
                if neighbor != parent:
                    if  dfs(neighbor,node):
                        return True
            colors[node]=2
            return False
        for i in range(n):
            if colors[i]!=0:
                continue
            if dfs(i,-1):
                return True
        return False
