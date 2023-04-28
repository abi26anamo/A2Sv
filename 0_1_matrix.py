class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        self.res = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j))
        def inbound(row,col):
            return 0<=row<len(mat) and 0<=col<len(mat[0])

        while queue:
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            n = len(queue)
            for _ in range(n):
                r,c = queue.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if inbound(row,col) and mat[row][col]==1 and (row,col) not in visited:
                        self.res[row][col]= self.res[r][c]+1
                        queue.append((row,col))
                        visited.add((row,col))
        return self.res
