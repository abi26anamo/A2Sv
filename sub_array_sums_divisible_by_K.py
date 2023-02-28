class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic =defaultdict(int)
        subsum =0
        count =0
        dic[0]=1
        for i in range(len(nums)):
            subsum+=nums[i]
            rem = subsum%k
            count+=dic[rem]
            dic[rem]+=1  
        return count
