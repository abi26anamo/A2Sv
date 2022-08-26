class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n= len(senate)
        D=deque()
        R = deque()
        for i,c in enumerate(senate):
            if c =="R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(n+r)
            else:
                D.append(n+d)
        return "Dire" if D else "Radiant"
                
        
        
        
        
        
        
        
        
        
        

            
        