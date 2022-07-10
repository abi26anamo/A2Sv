class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        lsum =0
        rsum =total
        for i in range(len(nums)):
            rsum -=nums[i]
            if rsum == lsum:
                return i
            lsum+=nums[i]
        return -1