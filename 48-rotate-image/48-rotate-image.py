class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N=len(matrix)
        for i in range(N):
            for c in range(i):
                matrix[i][c],matrix[c][i] = matrix[c][i],matrix[i][c]
        for i in matrix:
            i.reverse()
        