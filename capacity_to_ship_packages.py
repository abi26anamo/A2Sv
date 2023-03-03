class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isGood(capacity):
            n = len(weights)
            curr_sum=0
            curr_day =0
            for right in range(n):
                curr_sum+=weights[right]
                if curr_sum < capacity and right == n-1:
                    curr_day+=1
                elif curr_sum > capacity:
                    if right == n-1:
                        curr_day+=1
                    curr_day+=1
                    curr_sum = weights[right]
                elif curr_sum == capacity:
                    curr_day+=1
                    curr_sum =0
            if curr_day <= days:
                return True
            else:
                return False

        left = max(weights)-1
        right = sum(weights)

        while left+1 < right:
            mid  = left+(right-left)//2
            if isGood(mid):
                right =mid
            else:
                left = mid
        return right
