class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n==0 or citations[-1]==0:
            return 0
        if n==1 and citations[-1]!=0:
            return 1

        left,right = -1,n

        while left+1 < right:
            mid = left+(right-left)//2

            if n-mid > citations[mid]:
                left = mid
            else:
                right = mid
        return n-right
