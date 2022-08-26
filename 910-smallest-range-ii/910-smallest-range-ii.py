class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n =len(nums)
        res =nums[n-1]- nums[0]
        for i in range(n-1):
            j=i+1
            minm = min(nums[0]+k,nums[j]-k)
            maxm = max(nums[i]+k,nums[n-1]-k)
            res = min(res,maxm-minm)
        return res
        
            
        
        
        
        
        

            