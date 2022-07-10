class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        N=len(arr)
        tot =0
        for i in range(1,N+1,2):
            for t in range(N-i+1):
                tot+=sum(arr[t:t+i])
        return tot