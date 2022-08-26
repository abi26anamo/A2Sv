class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sort_ed = sorted(str(n))
        s = 1
        while s <=10**9:
            if sorted(str(s)) == sort_ed:
                return True
            s*=2
        return False
#         c= Counter([int(n) for i in str(n)])
#         n=0
#         i=0
#         while n <=10**9:
#             n=2**i
#             d= Counter([int(i) for i in str(n)])
#             if c ==d:
#                 return True
#             i+=1
#         return False
        
        
                    
      
            
        