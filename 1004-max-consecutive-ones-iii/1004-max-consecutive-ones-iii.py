class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start =0
        maxones =0
        freq ={}
        max_len =0
        
        for i in range(len(nums)):
            if nums[i] not in  freq :
                freq[nums[i]] = 0
            if nums[i]==1:
                freq[nums[i]]+=1
            maxones = max(freq[nums[i]],maxones)
            
            if (i-start+1 - maxones) >k:
                freq[nums[start]]-=1
                start+=1
        max_len = max(max_len,i-start+1)
        return max_len
                
            
        