class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixsum =[sum(nums[:i+1]) for i in range(len(nums))]
        minsum = min(prefixsum)
        if minsum <=0:
            return abs(minsum)+1
        else:
            return 1