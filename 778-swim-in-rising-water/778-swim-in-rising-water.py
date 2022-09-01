class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        mnheap = [(grid[0][0],0,0)]
        res =0
        N = len(grid)
        M = len(grid[0])
        visited = set()
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        
        while mnheap:
            mx,r,c = heapq.heappop(mnheap)
            res = max(mx,res)
            if (r,c) ==(N-1,M-1):
                break
            for dr,dc in direction:
                row,col = r+dr,c+dc
                if 0<=row<N and 0<=col<M and (row,col) not in visited:
                    heapq.heappush(mnheap,(grid[row][col],row,col))
                    visited.add((row,col))
        return res
        