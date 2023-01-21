class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        nums.sort()
        
        for i in range(len(nums)):
            dic[nums[i]].append(i)
            
        return dic[target]
