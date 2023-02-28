class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n+1)]
        
        #build the prefix sum
        for i in range(1,n+1):
            prefix[i] = prefix[i-1]+nums[i-1]
        
        count =0
        hash_map =defaultdict(int)
        
        for right in range(len(prefix)):
            if prefix[right]-k in hash_map:
                count+=hash_map[prefix[right]-k]
                hash_map[prefix[right]]+=1
            else:
                hash_map[prefix[right]]+=1
        
        return count
        
        
