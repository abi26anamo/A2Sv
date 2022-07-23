class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic ={}
        ans = []
        for i in range(len(nums)):
            if nums[i] in dic:
                ans.append(nums[i])
            dic[nums[i]] =i
        return ans
            