class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for l in range(len(arr)-1,-1,-1):
            i,_ = max(enumerate(arr[:l+1]), key=lambda x: x[1]) 
            if i != l:
                arr[:i+1] = arr[:i+1][::-1]
                arr[:l+1] = arr[:l+1][::-1]
                res.extend([i+1,l+1])
        return res 