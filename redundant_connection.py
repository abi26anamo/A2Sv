class UnionFind:
    def __init__(self,n):
        self.n = n
        self.rep = [i for i in range(n+1)]

    def find(self,x):
        if self.rep[x]==x:
            return x
        curr = self.find(self.rep[x])
        self.rep[x] = curr
        return curr

    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)

        if xrep!=yrep:
            self.rep[yrep]=xrep

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        redx,redy = 0,0
        n = len(edges)
        uf = UnionFind(n)
        for u,v in edges:
            if uf.find(u)==uf.find(v):
                redx,redy = u,v
            uf.union(u,v)
        return [redx,redy]
