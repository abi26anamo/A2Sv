class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left =0
        right = len(nums)-1
        while left <right:
            mid = (left+right)//2
            count=(sum(i<=mid for i in nums))
            if count <= mid:
                left = mid+1
            else:
                right= mid
        return right