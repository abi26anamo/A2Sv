class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = len(queries)
        pre_req = [[float("inf")]*(numCourses) for _ in range(numCourses)]
        for p,s  in prerequisites:
            pre_req[p][s] =1
        
        for i in range(numCourses):
            pre_req[i][i] = 0
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if pre_req[i][j] > pre_req[i][k]+pre_req[k][j]:
                        pre_req[i][j] = pre_req[i][k]+pre_req[k][j]  
        res = []
        for query in queries:
            if pre_req[query[0]][query[1]] != float('inf'):
                res.append(True)
            else:
                res.append(False)   
        return res
