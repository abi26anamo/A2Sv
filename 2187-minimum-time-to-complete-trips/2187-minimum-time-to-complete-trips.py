class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left =0
        right = 10**20
        def good(x):
            count =0
            for t in time:
                count+=x//t
            return count>=totalTrips
        while left < right:
            mid = (left+right)//2
            if good(mid):
                right = mid
            else:
                left = mid+1
        return left
            
        