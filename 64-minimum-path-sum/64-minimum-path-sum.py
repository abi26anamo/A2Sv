class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        res = [[float('inf')]*(m+1)for r in range(n+1)]
        res[n-1][m] =0
        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                res[r][c]=grid[r][c]+min(res[r+1][c],res[r][c+1])
        return res[0][0]
        