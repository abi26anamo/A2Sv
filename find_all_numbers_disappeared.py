class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        start = 0
        res = []
        while start <n:
            correct_Idx = nums[start]-1
            if nums[start]!= nums[correct_Idx]:
                nums[start],nums[correct_Idx] = nums[correct_Idx],nums[start]
            else:
                start+=1
        for i in range(n):
            if nums[i]!=i+1:
                res.append(i+1)
        return res
