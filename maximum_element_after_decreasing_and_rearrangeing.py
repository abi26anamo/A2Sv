class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        if arr[0]!=1:
            arr[0]=1
        for i in range(n-1):
            if abs(arr[i]-arr[i+1])>1:
                arr[i+1] = arr[i]+1
            else:
                continue
        return arr[-1]
