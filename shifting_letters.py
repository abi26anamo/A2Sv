class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0]*n
        
        for start,end,dirc in shifts:
            if dirc == 0:
                prefix[start]-=1
                
                if end+1<n:
                    prefix[end+1]+=1
            else: 
                prefix[start]+=1
                
                if end+1<n:
                    prefix[end+1]-=1
                    
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
            
        for indx in range(n):
            val= (ord(s[indx])-ord('a')+prefix[indx]) %26
            output = ""
            if val >= 0:
                output = chr(ord("a") + val)
            else:
                output = chr(ord("z") - val)
            
            prefix[indx] = output
        
        
            
        return "".join(prefix)
        
    
