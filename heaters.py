class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        for i in range(len(houses)):
            left = 0
            right = len(heaters)-1 
            min_dist = float('inf')
            while left <= right:
                mid = (left+right)//2
                min_dist = min(min_dist,abs(houses[i]-heaters[mid]))
                if heaters[mid] < houses[i]: 
                    left = mid+1
                else:
                    right = mid-1

            max_radius = max(min_dist,max_radius)

        return max_radius
