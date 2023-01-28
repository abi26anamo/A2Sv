class Solution:
   
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        operations = 0
        while left<right:
            curr = nums[left]+nums[right]
            if curr ==k:
                operations+=1
                left+=1
                right-=1
            elif curr>k:
                right-=1
            else:
                left+=1
        return operations
