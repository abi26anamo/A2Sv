class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        max_idx = requests[0][1]
        for r in requests:
            max_idx = max(max_idx,r[1])
            
        range_sum = [0]*(max_idx+2)
        for r in requests:
            range_sum[r[0]]+=1
            range_sum[r[1]+1]-=1
        
        for i in range(1,len(range_sum)):
             range_sum[i]+=range_sum[i-1]
                  
        nums.sort(reverse = True)
        range_sum.sort(reverse= True)

        max_sum = 0
        i=0
        while range_sum[i]!=0:
            max_sum+=(range_sum[i]*nums[i])
            i+=1
        
        return max_sum%(10**9+7)
