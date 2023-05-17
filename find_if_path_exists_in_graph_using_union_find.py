class UnionFind:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self,x):
        if self.rep[x]  == x:
            return x
        curr = self.find(self.rep[x])
        self.rep[x] = curr
        return curr
    
    def union(self,x,y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        if self.size[x_rep]>self.size[y_rep]:
            self.rep[y_rep] = x_rep
            self.size[x_rep]+=self.size[y_rep]
        else:
            self.rep[x_rep] = y_rep
            self.size[y_rep]+=self.size[x_rep]

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = UnionFind(n)

        for u,v in edges:
            graph.union(u,v)
        
        return graph.find(source)==graph.find(destination)
