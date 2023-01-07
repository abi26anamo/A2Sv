class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        dic = {}
        for i,val in enumerate(nums):
            dic[val]=i
            
        for operation in operations:
            
            if operation[0] in dic:
                
                nums[dic[operation[0]]] = operation[1]
                dic[operation[1]] = dic[operation[0]]
                
        return nums
