class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        stfirst =0
        endfirst = firstLen
        stsecond = endfirst
        endsecond = endfirst+secondLen
        pfirst =0
        psecond =0
        ans =0
        n = len(nums)
        while endfirst <= n:
            pfirst =sum(nums[stfirst:endfirst])
            stsecond=endfirst
            endsecond = endfirst+secondLen
            while endsecond <=n:
                psecond= sum(nums[stsecond:endsecond])
                stsecond+=1
                endsecond+=1
                ans = max(ans,pfirst+psecond)
            stsecond = 0
            endsecond = secondLen
            while endsecond <= stfirst:
                psecond =sum(nums[stsecond:endsecond])
                stsecond+=1
                endsecond+=1
                ans = max(ans,pfirst+psecond)
            stfirst+=1
            endfirst+=1
        return ans
            
            
            
            
                
        