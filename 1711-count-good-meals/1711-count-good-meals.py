class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        count =0
        powersofTwo = [2**i for i in range(22)]
        dic = Counter(deliciousness)
        
        for item in dic:
            
            for target in powersofTwo:
                
                diff = target-item
            
                if diff in dic and diff==item:
                    count+=dic[item]*(dic[item]-1)//2
                    
                elif diff in dic and diff!=item:
                    count+=dic[item]*dic[diff]/2 
                    
        return int(count)%(10**9+7)
    
    
                    
                    
                
                    
     
        
            
            
            
            
           
                
            
                
        