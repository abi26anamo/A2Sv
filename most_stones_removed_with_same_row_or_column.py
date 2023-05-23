class Solution:  
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        self.rep = {(i,j):(i,j) for i, j in stones}
        self.size = {(i,j):1 for i,j in stones}

        for i in range(n):
            for j in range(n):
                    row1,col1 = stones[i]
                    row2,col2 = stones[j]

                    if row1 == row2 or col1 == col2:
                        self.union((row1,col1),(row2,col2))
        for i in range(n):
            for j in range(n):
                    row1,col1 = stones[i]
                    row2,col2 = stones[j]

                    if row1 == row2 or col1 == col2:
                        self.union((row1,col1),(row2,col2))
        print(self.rep)
        res = set()
        for row,col in stones:
            res.add(self.rep[(row,col)])
        return n - len(res)
    
    def find(self,x):
        if self.rep[x]==x:
            return x
        curr = self.find(self.rep[x])
        self.rep[x] = curr
        return curr
    
    def union(self,u,v):
        u_rep = self.find(u)
        v_rep = self.find(v)

        if self.size[u_rep]>self.size[v_rep]:
            self.rep[v_rep] = u_rep
            self.size[u_rep]+=self.size[v_rep]
        else:
            self.rep[u_rep] = v_rep
            self.size[v_rep]+=self.size[u_rep]
       
  
