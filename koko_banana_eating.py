class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isGood(k):
            number_of_hours = 0
            for pile in piles:
                number_of_hours+=ceil(pile/k)

            if number_of_hours<=h:
                return True
            else:
                return False
        
        left = 0
        right = max(piles)+1
        while left+1 < right:
            mid = left+(right - left)//2

            if isGood(mid):
                right = mid
            else:
                left = mid
        return right
                
