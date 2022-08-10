class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lenRow =len(grid)
        lenCol = len(grid[0])
        visit = set()
        def dfs(row,col):
            if row<0 or row==lenRow or col<0 or col ==lenCol or grid[row][col]==0 or (row,col) in visit:
                return 0
            visit.add((row,col))
            return 1+dfs(row+1,col)+dfs(row-1,col)+dfs(row,col+1)+dfs(row,col-1)
        ans = 0
        for row in range(lenRow):
            for col in range(lenCol):
                ans = max(ans,dfs(row,col))
        return ans
                