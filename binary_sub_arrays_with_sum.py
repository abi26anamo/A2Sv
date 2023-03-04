class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        arr = [0,0,0,0,0]
        [0,0,0,0,0]
        """
        n = len(nums)
        hash_map  = {0:1}
        prefix_sum = 0
        count = 0

        for right in range(n):
            prefix_sum+=nums[right]

            if prefix_sum - goal in hash_map:
                count+=hash_map[prefix_sum-goal]

            if prefix_sum in hash_map:
                hash_map[prefix_sum]+=1
            else:
                hash_map[prefix_sum]=1
        return count
    
