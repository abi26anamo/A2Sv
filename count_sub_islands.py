class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid1)
        m = len(grid1[0])
        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        visited = set()
        self.valid = True
        def dfs(row,col):
            directions = [(-1,0),(0,-1),(0,1),(1,0)]
            visited.add((row,col))
            if not grid1[row][col]:
                self.valid = False
            for r,c in directions:
                new_row = row+r
                new_col = col+c
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid2[new_row][new_col]==1:
                    dfs(new_row,new_col)
            return self.valid
        sub_islands =0
        for r in range(n):
            for c in range(m):
                if (r,c) not in visited and grid2[r][c]==1:
                   if  dfs(r,c):
                       sub_islands+=1
                self.valid = True
        return sub_islands


