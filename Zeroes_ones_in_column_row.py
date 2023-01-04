class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        rows =[0]*n
        cols =[0]*m
        diff = [[0]*n]*m
        for i in range(n):
            for j in range(m):
                rows[i]+=grid[i][j]
                cols[j]+=grid[i][j]
        
        res =[]   
        for r in range(len(rows)):
            temp=[]
            for c in range(len(cols)):
                temp.append(rows[r]+cols[c]-(n-rows[r]+m-cols[c]))
            res.append(temp)
                
        return res
