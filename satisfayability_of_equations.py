class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        self.rep = {}
        self.size = {}
        for equ in equations:
            self.rep[equ[0]] = equ[0]
            self.rep[equ[-1]] = equ[-1]
            self.size[equ[0]] = 1
            self.size[equ[-1]] = 1

        for u,equal,_,v in equations:
            if equal == '=':
                self.union(u,v)
        for u,equal,_,v in equations:
            v_rep = self.find(v)
            u_rep = self.find(u)
            if v_rep == u_rep and  equal!='=':
                return False
        return True
    
    def find(self,x):
        if self.rep[x] ==x:
            return x
        curr = self.find(self.rep[x])
        self.rep[x]= curr
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
        


        
            
    
        
        
    
