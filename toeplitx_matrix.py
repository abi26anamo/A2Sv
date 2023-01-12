class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        dic = defaultdict(list)
        for r in range(n):
            for c in range(m):
                dic[r-c].append(matrix[r][c])
                
        for _,val in dic.items():
            if len(set(val))!=1:
                return False
        return True
                
                
        
