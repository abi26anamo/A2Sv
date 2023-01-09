class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        frequency_of_rows = {}
        grid_length = len(grid)
        equal_row_col_pairs = 0
        
        # iterate over the rows
        for row in range(grid_length):
            current_row = []
            
            #iterate over the columns and store the column elemnts of current_row
            for col in range(grid_length):
                current_row.append(grid[row][col])
                
            #convert mutable list to immutable string to use as key in frequency_count    
            current_row = str(current_row)
            # increase the count of the current_row is already present
            if current_row in frequency_of_rows:
                frequency_of_rows[current_row]+=1
                
            else:
                frequency_of_rows[current_row]=1
                
                
                
        for row in range(grid_length):
            
            current_col = []
            #itrate over the column and store the elements of the current_column
            for col in range(grid_length):
                current_col.append(grid[col][row])
                
            current_col = str(current_col)
            #check if current_col is in the dictionary of rows
            if current_col in frequency_of_rows:
                
                #column is in the dictionary of the rows increase our pairs by the frequency of the rows
                equal_row_col_pairs+=frequency_of_rows[current_col]
                
            else:
                continue
                
        return equal_row_col_pairs
