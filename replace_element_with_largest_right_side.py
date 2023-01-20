class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxm = -1
        for i in range(n-1,-1,-1):
            arr[i],maxm = maxm,max(maxm,arr[i])
        return arr
    
