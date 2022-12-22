class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n=len(nums)
        num = sorted(nums) 
        i = 0
        j = 2
        maxper = 0
        while j<n:
            if (num[i]+num[i+1])>num[j]:
                per = num[i]+num[i+1]+num[j]
                maxper = max(maxper,per)
            i+=1
            j+=1
        return maxper
        
       