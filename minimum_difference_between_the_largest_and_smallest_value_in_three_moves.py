class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n<=3:
            return 0
            
        first_two_last_one= nums[-2]-nums[2]
        last_two_first_one = nums[-3]-nums[1] 
        last_three = nums[-4]-nums[0]
        first_three = nums[-1]-nums[3]

        return min(last_three,first_three,first_two_last_one,last_two_first_one)

        

            
        
        

       
