class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols = len(matrix),len(matrix[0])
        
        #build column matrix
        for row in range(1,rows):
            matrix[row][0]+=matrix[row-1][0]
            
        #build row matrix
        for col in range(1,cols):
            matrix[0][col] +=matrix[0][col-1]
            
        for row in range(1,rows):
            for col in range(1,cols):
                matrix[row][col] = matrix[row-1][col]+matrix[row][col-1]-matrix[row-1][col-1]+matrix[row][col]
        
        self.matrix = matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        up_right = self.matrix[row1-1][col2] if row1 else 0
        bottom_left = self.matrix[row2][col1-1] if col1 else 0
        diagonal = self.matrix[row1-1][col1-1] if (row1 and col1) else 0
        return self.matrix[row2][col2]-up_right-bottom_left+diagonal
    
