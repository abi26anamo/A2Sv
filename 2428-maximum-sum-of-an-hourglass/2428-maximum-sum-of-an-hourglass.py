class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n= len(grid)
        m = len(grid[0])
        maxsum=0
        for i in range(1,n-1):
            for j in range(1,m-1):
                curr =0
                curr+=sum(grid[i-1][j-1:j+2])
                curr+=sum(grid[i+1][j-1:j+2])
                curr+=grid[i][j]
                maxsum = max(maxsum,curr)
        return maxsum
                
        