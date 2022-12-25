class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res =''
        n= len(word1)
        m =len(word2)
        i=0
        j=0
        
        while i<n and j<m:
                res+=word1[i]
                res+=word2[j]
                i+=1
                j+=1
                
        while i<n:
            res+=word1[i]
            i+=1
            
        while j<m:
            res+=word2[j]
            j+=1
            
        return res
        
        
        