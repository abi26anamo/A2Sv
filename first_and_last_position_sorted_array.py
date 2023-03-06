class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       res = [-1,-1]
       left,right = -1,len(nums)
       while left+1 < right:
           mid = left+(right-left)//2

           if nums[mid]<target:
               left = mid
           else:
               right = mid
       res[0]=right

       
       left,right = -1,len(nums)
       while left+1 < right:
           mid = left+(right-left)//2

           if nums[mid]>target:
               right = mid
           else:
               left = mid
       res[1]=left
       return res if target in nums else [-1,-1]
