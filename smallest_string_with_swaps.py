class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.rep = [i for i in range(n)]
        self.size = [1 for i in range(n)] 
        for i,j in pairs:
            self.union(i,j)

        sameConnections = defaultdict(list)
        for i in range(n):
            parent = self.find(i)
            sameConnections[parent].append(s[i])
        
        for key,values in sameConnections.items():
            values.sort(reverse= True)
 
        result = []
        for i in range(n):
            parent = self.find(i)
            result.append(sameConnections[parent].pop())
        return "".join(result)
        
    def find(self, x):
        if self.rep[x] == x:
            return x
        curr = self.find(self.rep[x])
        self.rep[x] = curr
        return curr

    def union(self, u, v):
        u_rep = self.find(u)
        v_rep = self.find(v)

        if self.size[u_rep] > self.size[v_rep]:
            self.rep[v_rep] = u_rep
            self.size[u_rep] += self.size[v_rep]
        else:
            self.rep[u_rep] = v_rep
            self.size[v_rep] += self.size[u_rep]
