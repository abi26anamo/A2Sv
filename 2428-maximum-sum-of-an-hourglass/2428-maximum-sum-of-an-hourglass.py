class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n= len(grid)
        m = len(grid[0])
        maxsum=0
        for i in range(1,n-1):
            for j in range(1,m-1):
                s =0
                s+=sum(grid[i-1][j-1:j+2])
                s+=sum(grid[i+1][j-1:j+2])
                s+=grid[i][j]
                maxsum = max(maxsum,s)
        return maxsum
                
        