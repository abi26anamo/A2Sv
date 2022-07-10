class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        indexOne =0
        indextwo = [0,k]
        indexthree = [0,k,k*2]
        
        maxonesum = sum(nums[:k])
        maxtwosum = sum(nums[:k*2])
        maxthreesum = sum(nums[:k*3])
        
        curonesum = sum(nums[:k])
        curtwosum = sum(nums[k:k*2])
        curthreesum = sum(nums[k*2:k*3])
        
        n=len(nums)
        for i in range(1,n-k*3+1):
            curonesum = curonesum-nums[i-1]+nums[i+k-1]
            curtwosum = curtwosum-nums[i+k-1] +nums[i+k*2-1]
            curthreesum = curthreesum -nums[i+k*2 -1] + nums[i+k*3-1]
            if curonesum > maxonesum:
                indexOne =i
                maxonesum = curonesum
            if curtwosum+maxonesum > maxtwosum:
                indextwo = [indexOne,i+k]
                maxtwosum = curtwosum+maxonesum
            if curthreesum + maxtwosum > maxthreesum:
                indexthree = indextwo + [i+k*2]
                maxthreesum = curthreesum + maxtwosum
        return indexthree
                
                
            
       