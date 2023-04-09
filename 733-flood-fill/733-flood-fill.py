class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        N,M = len(image),len(image[0])
        #function that checks valid boundary
        def inbound(row,col):
            return  0<=row<N and 0<=col < M

        def dfs(grid,row,col,new_color):
            start_color = grid[row][col]
            grid[row][col] = new_color

            directions = [(-1,0),(0,-1),(0,1),(1,0)]

            for r,c in directions:
                new_row = row+r
                new_col = col+c

                if inbound(new_row,new_col) and grid[new_row][new_col]==start_color and grid[new_row][new_col]!=new_color:
                    
                    dfs(grid,new_row,new_col,new_color)
        dfs(image,sr,sc,color)
        return image

        
