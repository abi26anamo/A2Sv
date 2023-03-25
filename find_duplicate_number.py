class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        start =0
        while start < n:
            correct_Idx = nums[start]-1
            if start < n and nums[start]!=nums[correct_Idx]:
                nums[start],nums[correct_Idx] = nums[correct_Idx],nums[start]
            else:
                start+=1
        for i in range(n):
            if nums[i]!=i+1:
                return nums[i]
        return n
