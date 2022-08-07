class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n= len(citations)
        if n ==0 or citations[-1] ==0:
            return 0
        high=n
        low = 0
        while low < high:
            mid = (low+high)//2
            if n-mid > citations[mid]:
                low = mid+1
            else:
                high = mid
        return n-low
        
        
        
        
        
        
        
        
        
        
       