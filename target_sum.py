class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dp(i,curr_target):
            ways = 0
            if i == n and curr_target == 0:
                return 1
            if i == n and curr_target != 0:
                return 0
            if (i,curr_target) in memo:
                return memo[(i,curr_target)]
            
            ways+=dp(i+1,curr_target-nums[i])
            ways+=dp(i+1,curr_target+nums[i])
            memo[(i,curr_target)] = ways
            return ways
        return dp(0,target)
