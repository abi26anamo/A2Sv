class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for a, b in dislikes:
            adjList[a - 1].append(b - 1)
            adjList[b - 1].append(a - 1)

        BLACK = 1
        RED = -1
        colors = [0] * n
        
        def dfs(node, prevCol=BLACK):
            currColor = -prevCol
            colors[node] = currColor
            for nextNode in adjList[node]:
                if colors[nextNode] != 0 and colors[node] == colors[nextNode]:
                    return False
                if colors[nextNode] == 0 and not dfs(nextNode, currColor):
                    return False
            return True
        
        for node in range(n):
            if colors[node] == 0 and not dfs(node):
                return False
        return True
       
        