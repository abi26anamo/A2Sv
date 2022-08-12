class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    count[node] += count[neighbor]
                    ans[node] += ans[neighbor] + count[neighbor]
        
        def dfs2(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    ans[neighbor] = ans[node] - count[neighbor] + (n - count[neighbor])
                    dfs2(neighbor)
            
        graph = defaultdict(list)
        
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
            
        count = [1 for _ in range(n)]
        ans = [0 for _ in range(n)]
        
        visited = set()
        dfs(0)
        visited = set()
        dfs2(0)
        
        return ans
        
        
        
        
        
      