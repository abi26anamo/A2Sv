class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arr =[]
        for i in range(n+1):
            arr.append(i)
        for i in arr:
            if i not in nums:
                return i
     
        
            
      
            
        
        