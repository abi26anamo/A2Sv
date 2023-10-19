from collections import defaultdict

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if total % 2 == 1:
            return False
        else:
            partition_sum = total // 2
            memo = defaultdict(dict)

            def dp(nums, i, partition_sum):
                if i >= len(nums):
                    return False

                if partition_sum == 0:
                    return True

                if i in memo and partition_sum in memo[i]:
                    return memo[i][partition_sum]

                if nums[i] <= partition_sum:
                    if dp(nums, i + 1, partition_sum - nums[i]):
                        memo[i][partition_sum] = True
                        return True
                memo[i][partition_sum] = dp(nums, i + 1, partition_sum)
                return memo[i][partition_sum]
            return dp(nums, 0, partition_sum)

