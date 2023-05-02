class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        visited = set()

        def inbound(row,col):
            return 0<=row<len(maze) and 0<=col<len(maze[0])
        queue.append((entrance[0],entrance[1],0))
        visited.add((entrance[0],entrance[1]))
        while queue:
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            n = len(queue)
            r,c,shortest_exit = queue.popleft()
            if shortest_exit!=0 and (r==0 or c==0 or r==len(maze)-1 or c == len(maze[0])-1 and maze[r][c]=="."):
                return shortest_exit
            for dr,dc in directions:
                row,col = r+dr,c+dc
                if inbound(row,col) and maze[row][col]=="." and (row,col) not in visited:
                    queue.append((row,col,shortest_exit+1))
                    visited.add((row,col))
        return -1
        
