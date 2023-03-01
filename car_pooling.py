class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix= [0]*1001
        
        for trip in trips:
            prefix[trip[1]]+=trip[0]
            prefix[trip[2]]-=trip[0]
        
        if prefix[0]>capacity:
            return False
        
        for i in range(1,1001):
            prefix[i]+=prefix[i-1]
            
            if prefix[i]>capacity:
                return False
        return True
