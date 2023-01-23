class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        
        for rightidx in range(len(arr)-1,-1,-1):
            new_arr = enumerate(arr[:rightidx+1])
            
            index,_ = max(new_arr, key=lambda x: x[1]) 
            
            if index!= rightidx:
                
                arr[:index+1] = arr[:index+1][::-1]
                arr[:rightidx+1] = arr[:rightidx+1][::-1]
                res+=[index+1,rightidx+1]
                
        return res 
    
