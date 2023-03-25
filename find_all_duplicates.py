class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        start = 0
        ans = []
        while start < n:
            correct_Idx = nums[start]-1
            if nums[start]!=nums[correct_Idx]:
                nums[start],nums[correct_Idx] = nums[correct_Idx],nums[start]
            else:
                start+=1
        for i in range(n):
            if nums[i]!=i+1:
                ans.append(nums[i])
        return ans
