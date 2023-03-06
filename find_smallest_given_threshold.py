class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isgood(val):
             result = sum([ceil(num/val) for num in nums])
             if result <= threshold:
                 return True
             else:
                 return False
        left,right = 0,max(nums)
        while left+1 <right:
            mid = left+(right-left)//2
            if isgood(mid):
                right = mid
            else:
                left = mid
        return right
