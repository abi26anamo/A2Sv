class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n=len(order)
        dic ={}
        for i in range(n):
            dic[order[i]]=i
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j]!=w2[j]:
                    if dic[w1[j]] > dic[w2[j]]:
                        return False
                    break
        return True
            
            
      
        
  
    
        
       
