class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area =0
        while left<=right:
            min_height = min(height[left],height[right])
            runnig_area = (right-left)*min_height
            if height[right]>height[left]:
                left+=1
            else:
                right-=1

            max_area = max(max_area,runnig_area)

        return max_area
    
            
