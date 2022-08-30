class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
  
        N=len(matrix)
        for i in range(N):
            for c in range(i):
                matrix[i][c],matrix[c][i] = matrix[c][i],matrix[i][c]
        for i in matrix:
            i.reverse()




    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            self.rotate(mat)
            if mat == target:
                return True
        return False
