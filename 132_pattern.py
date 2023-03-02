class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_arr = [0]*n
        min_arr[0] = nums[0]
        for i in range(1,n-1):
            min_arr[i] = min(min_arr[i-1],nums[i])
            
        stack = [] 
        for i in range(n-1,0,-1):
            
            while stack and stack[-1]<=min_arr[i-1]:
                stack.pop()
            
            if stack and stack[-1]<nums[i]:
                return True
            
            stack.append(nums[i])

        return False
            
