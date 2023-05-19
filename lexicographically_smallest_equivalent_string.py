class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.rep = {chr(97+i):chr(97+i) for i in range(27)}
        n = len(baseStr)
        for i in range(len(s1)):
            self.union(s1[i],s2[i])


        res = ""
        for i in range(n):
            res+=self.find(baseStr[i])
        return res
    
    def find(self,x):
            if self.rep[x]==x:
                return x
            curr = self.find(self.rep[x])
            self.rep[x] = curr
            return curr
        
    def union(self,u,v):
            u_rep = self.find(u)
            v_rep = self.find(v)

            if u_rep < v_rep:
                self.rep[v_rep]= u_rep

            else:
                self.rep[u_rep]  = v_rep
            
