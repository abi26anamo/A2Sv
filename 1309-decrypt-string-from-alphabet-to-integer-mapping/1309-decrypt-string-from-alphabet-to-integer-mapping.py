class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        i=0
        res =[]
        
        while i<n:
            if i+2<n and s[i+2]=='#':
                    char = chr(int(s[i:i+2])+64)
                    res.append(char)
                    i+=3
            else:
                char =chr(int(s[i])+64)
                res.append(char)
                i+=1
        return "".join(res).lower()
          
                
                

        
        
        

            
       
