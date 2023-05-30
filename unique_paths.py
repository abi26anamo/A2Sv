class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(r,c):
            if r == m or c ==n:
                return 1
            
            if 0<=r < m and 0<=c < n and (r,c) not in memo:
                memo[(r,c)] = dp(r,c+1) + dp(r+1,c)
            if  0<=r < m and 0<=c < n :
                return memo[(r,c)]
            
        return dp(1,1)
            
            
