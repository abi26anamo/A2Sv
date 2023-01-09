class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
                               
        def Xwin(grid):
            isover = False
            if board[0][0]==board[1][1]==board[2][2]=="X":
                isover= True
            if board[0][2] == board[1][1] == board[2][0]=="X":
                isover =True
            
            for i in range(3):
                if board[i][0]==board[i][1]==board[i][2]=="X":
                    isover= True
                    break
                elif board[0][i]==board[1][i]==board[2][i]=="X":
                    isover= True
                    break
            return isover
        
        
        def Owin(grid):
            isover = False
            if board[0][0]==board[1][1]==board[2][2]=="O":
                isover= True
            if board[0][2] ==board[1][1]==board[2][0]=="O":
                isover =True
            for i in range(3):
                if board[i][0]==board[i][1]==board[i][2]=="O":
                    isover= True
                    break
                elif board[0][i]==board[1][i]==board[2][i]=="O":
                    isover= True
                    break
            return isover

        x_count = 0
        o_count =0
        for i in range(3):
            for j in range(3):
                if board[i][j]=="X":
                    x_count+=1
                elif board[i][j]=="O":
                    o_count+=1
        if o_count > x_count or x_count-o_count>1:
            return False
        
        if Owin(board):
            if Xwin(board):
                return False
            return o_count == x_count
        
        if Xwin(board) and x_count!=o_count+1:
            return False

        return True
