class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(-1, 0), (0, 1)]
        }

        def inbound(r,c):
            return 0 <= r < m and 0 <= c < n
        
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return True
            
            visited.add((i, j))
            
            for dx, dy in directions[grid[i][j]]:
                nx, ny = i + dx, j + dy
                if  inbound(nx,ny) and (nx, ny) not in visited:
                    for nx_dx, nx_dy in directions[grid[nx][ny]]:
                        if nx + nx_dx == i and ny + nx_dy == j:
                            if dfs(nx, ny):
                                return True
            
            return False
        
        return dfs(0, 0)

