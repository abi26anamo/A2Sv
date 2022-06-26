class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pair = []
        nums.sort()
        for i in range(len(nums)//2):
            pair.append(nums[i]+nums[len(nums)-i-1])
        return max(pair)