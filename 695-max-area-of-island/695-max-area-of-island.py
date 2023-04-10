class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        graph = defaultdict(list)
        visited  = set()
    
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
     
        def dfs(row,col):
            directions = [(-1,0),(0,-1),(0,1),(1,0)]
            visited.add((row,col))
            for r,c in directions:
                new_row = row+r
                new_col = col+c
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col]==1:
                    dfs(new_row,new_col)

        max_area =0
        all_visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in all_visited:
                    dfs(i,j)
                max_area  = max(max_area,len(visited))
                for v in visited:
                    all_visited.add(v)
                visited = set()
        return max_area
                
