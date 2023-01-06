class Solution:
    def printVertically(self, s: str) -> List[str]:
        new_str =  s.split(" ")
        
        max_len =0
        for s in new_str:
            max_len = max(max_len,len(s))
        
        for i in range(len(new_str)):
            while len(new_str[i])<max_len:
                new_str[i]+=" "
                
                
        res = []
        for c in range(max_len):
            temp = []
            for r in range(len(new_str)):
                temp.append(new_str[r][c])
                s ="".join(temp)
            res.append(s.rstrip())
   
        return res
