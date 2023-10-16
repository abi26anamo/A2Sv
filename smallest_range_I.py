class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:            
        nums.sort()
        score = nums[-1]-nums[0]-2*k
        return score if score>0 else 0
