class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            temp = nums[0]
            counts = 1
            for i in range(1, len(nums)):
                if nums[i] != temp:
                    nums[counts] = nums[i]
                    temp = nums[i]
                    counts+=1
            return counts