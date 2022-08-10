class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M,N = len(board),len(board[0])
        def dfs(row,col):
            if row < 0 or row == M or col<0 or col == N or board[row][col]!='O':
                return
            board[row][col]='C'
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for row in range(M):
            for col in range(N):
                if board[row][col] =="O" and (row in [0,M-1 ]or col in [0,N-1]):
                    dfs(row,col)
                
        for row in range(M):
            for col in range(N):
                if board[row][col] =="O":
                    board[row][col]="X"
        for row in range(M):
            for col in range(N):
                if board[row][col] =="C":
                    board[row][col]="O"