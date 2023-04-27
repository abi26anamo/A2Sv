class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]:
            return -1
        shortest_length =0
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        while queue:
            directions = [(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if (r,c)==(n-1,n-1):
                    return shortest_length+1
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if row <0 or row == n or col <0 or col == n or grid[row][col]!=0 or (row,col) in visited:
                        continue
                    queue.append((row,col))
                    visited.add((row,col))
            shortest_length+=1
        return -1
