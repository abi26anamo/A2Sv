class UnionFind:
    def __init__(self, n):
        self.rep = [i for i in range(n+1)]
        self.size = [1]*(n+1)
        self.min = [float('inf') for _ in range(n+1)]

    def find(self,x):
        if self.rep[x]  == x:
            return x
        curr = self.find(self.rep[x])
        self.rep[x] = curr
        return curr
    
    def union(self,x,y,cost):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if self.size[x_rep]<self.size[y_rep]:
            x_rep,y_rep = y_rep,x_rep
        self.min[x_rep] = min(self.min[x_rep],self.min[y_rep],cost)

        if x_rep!=y_rep:
            self.rep[y_rep]=x_rep
            self.size[x_rep] += self.size[y_rep]
        
        
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph= UnionFind(n) 
        dist = float('inf')  
        for u,v, d in roads:
          graph.union(u,v,d)
        return graph.min[graph.find(1)]
