class Solution:
    def findMin(self, nums: List[int]) -> int:
        left =0
        right = len(nums)-1
        minimum =nums[0]
        while left<=right:
            mid = (left+right)//2
            if nums[mid] < minimum:
                minimum = nums[mid]
                right = mid-1
            else:
                left= mid+1
        return minimum
                
        
            