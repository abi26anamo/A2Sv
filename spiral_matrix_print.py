class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        spiral_order =[]
        curr_first_row,curr_last_row = 0,len(matrix)
        curr_first_column,curr_last_column = 0,len(matrix[0])
        
        
        while curr_first_row <curr_last_row and curr_first_column <curr_last_column:
            
            #iterate over the first row and update it by one
            for point in range(curr_first_column,curr_last_column):
                spiral_order.append(matrix[curr_first_row][point])
            curr_first_row+=1
            
            #iterate over the last column and update it by one
            for point in range(curr_first_row,curr_last_row):
                spiral_order.append(matrix[point][curr_last_column-1])
            curr_last_column-=1

            #handle edge cases
            if curr_first_row>=curr_last_row or curr_first_column>=curr_last_column:
                break
                
            #iterate over the last row and update it by one
            for point in range(curr_last_column-1,curr_first_column-1,-1):
                spiral_order.append(matrix[curr_last_row-1][point])
            curr_last_row-=1
            
            #iterate over the first column and update it by one
            for point in range(curr_last_row-1,curr_first_row-1,-1):
                spiral_order.append(matrix[point][curr_first_column])
            curr_first_column+=1
                
        return spiral_order
                
