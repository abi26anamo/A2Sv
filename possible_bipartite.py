class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        color = [-1]*(n+1)
        visited = set()
        def dfs(node,node_color):
            color[node]=node_color
            visited.add(node)
            for vertex in graph[node]:
                if vertex not in visited:
                    if color[vertex] == -1:
                        if not  dfs(vertex,1-node_color):
                            return False
                elif color[vertex]==node_color:
                    return False
            return True

        for vertex in graph:
            if vertex not in visited:
                if not dfs(vertex,0):
                    return False
        return True
