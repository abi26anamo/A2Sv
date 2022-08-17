class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        minute =0
        fresh =0
        M= len(grid)
        N = len(grid[0])
        for r in range(M):
            for c in range(N):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c] ==2:
                    queue.append([r,c])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue and fresh >0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if row <0 or row == len(grid) or col <0 or col == len(grid[0]) or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    queue.append([row,col])
                    fresh-=1
            minute+=1
        return minute if fresh == 0 else -1
                    
                    