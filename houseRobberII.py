class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return nums[0]
        return max(self.houseRobberI(nums[1:]),self.houseRobberI(nums[:-1]))


    def houseRobberI(self,arr):
        n = len(arr)
        memo = [-1 for _ in range(n)]
        if n==1:
            return arr[0]
        if n==2:
            return max(arr[0],arr[1])
        
        memo[0]=arr[0]
        memo[1]=max(arr[0],arr[1])
        for i in range(2,n):
            if memo[i]==-1:
                memo[i] = max(memo[i-1],memo[i-2]+arr[i])
        return memo[n-1]
       
