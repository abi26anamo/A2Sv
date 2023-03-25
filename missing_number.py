class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       n = len(nums)
       start = 0
       while start <n :
           correct_pos = nums[start]
           if correct_pos < n and correct_pos!=start:
               nums[start],nums[correct_pos] = nums[correct_pos],nums[start]
           else:
               start+=1

       for i in range(n):
           if nums[i]!=i:
               return i 
       return n
