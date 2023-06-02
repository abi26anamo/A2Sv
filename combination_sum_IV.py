class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i,amount):
            paths = 0
            if amount == 0:
                return 1
            if amount <0:
                return 0
            if (i,amount) in memo:
                return memo[(i,amount)]
            for idx in range(len(nums)):
                paths+=dp(idx,amount-nums[idx])
            memo[(i,amount)] = paths
            return paths
        return dp(0,target)
