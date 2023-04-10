class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(set)
        res = []
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    graph[i+1].add(j+1)
                    graph[j+1].add(i+1)

        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for vertex in graph:
            if vertex not in visited:
                provinces = set()
                dfs(vertex)
                for v in visited:
                    provinces.add(v)
            if provinces not in res:
                   res.append(provinces)
            visited = set()
        return len(res)
            



        
       
