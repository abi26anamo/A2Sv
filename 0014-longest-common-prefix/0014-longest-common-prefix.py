class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = len(strs[0])
        res =''
        
        for i in range(n):
            
            for s in strs:
                if i == len(s) or s[i]!=strs[0][i]:
                    return res
                
            res+=strs[0][i]
            
        return res
            
        
        




                
                


         
       
        