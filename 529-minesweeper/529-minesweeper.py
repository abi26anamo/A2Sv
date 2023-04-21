class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def helper(board, i, j):
            m, n = len(board), len(board[0])
            if i<0 or j<0 or i>=m or j>=n or board[i][j] != 'E':
                return

            directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

            adjecent = 0

            for d in directions:
                di, dj = i + d[0], j + d[1]
                if 0 <= di < m and 0 <= dj < n and board[di][dj] == 'M':        
                    adjecent += 1

            if adjecent == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(adjecent)
                return

            for d in directions:
                di, dj = i + d[0], j + d[1]
                helper(board, di, dj)
        i, j = click[0], click[1]

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        helper(board, i, j)
        return board
