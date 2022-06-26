import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        MAX = sys.maxsize
        shortest = MAX
        Sum =0
        while (j< len(nums)):
            Sum+=nums[j]
            if Sum >= target:
                while Sum >=target:
                    Sum-=nums[i]
                    i+=1
                shortest = min(shortest,j-i+2)
            j+=1
        return 0 if shortest == MAX else shortest

