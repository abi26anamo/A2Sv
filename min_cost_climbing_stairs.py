class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1 for _ in range(n)]
        if n==2:
            return min(cost[0],cost[1])
        memo[0] = cost[0]
        memo[1]= cost[1]

        for i in range(2,n):
            if memo[i]==-1:
                 memo[i] = cost[i]+min(memo[i-1],memo[i-2])
        return min(memo[n-1],memo[n-2])
