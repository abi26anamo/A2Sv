class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        res =0
        
        for num,val in count.items():
            res+=val*(val-1)//2
        return res
         
        
            