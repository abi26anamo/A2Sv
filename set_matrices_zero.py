class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_with_zero = set()
        cols_with_zero = set()
        len_row = len(matrix)
        len_col = len(matrix[0])
        
        for row in range(len_row):
            for col in range(len_col):
                if matrix[row][col] ==0:
                    rows_with_zero.add(row)
                    cols_with_zero.add(col)
                    
        for row in rows_with_zero:
            for col in range(len_col):
                matrix[row][col]=0
                
        for col in cols_with_zero:
            for row in range(len_row):
                matrix[row][col]=0
        
