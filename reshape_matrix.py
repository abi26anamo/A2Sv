class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n*m!=r*c:
            return mat
        else:
            one_D = [0]*(c*r)

            for i in range(n):
                for j in range(m):
                    one_D[i*m+j] = mat[i][j]
                   
                    
            reshaped = [[0]*c for _ in range(r)]
            
            for i in range(len(one_D)):
                reshaped[i//c][i%c] = one_D[i]

            return reshaped
