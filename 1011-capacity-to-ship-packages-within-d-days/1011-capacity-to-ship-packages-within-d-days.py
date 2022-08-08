class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right, n = max(weights), sum(weights), len(weights)
        
        while left < right:
            cap = int((right + left)/2)
            curr, curr_days = 0, 0
            for weight in weights:
                if curr+weight > cap:
                    curr = weight
                    curr_days += 1
                else:
                    curr += weight
            
            if curr_days >= days:
                left = cap+1
            else:
                right = cap
            
        return left