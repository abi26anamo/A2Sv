class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        answer = []
        for rich,poor in richer:
            graph[poor].append(rich)
        def dfs(node,visited):
            if not graph[node]:
                return node
            loud= node
            visited.add(node)
            for neighbor in graph[node]:
                if quiet[neighbor]<=quiet[loud]:
                    loud = neighbor
                if neighbor not in visited:
                    curr = dfs(neighbor,visited)
                    if quiet[curr]<quiet[loud]:
                        loud = curr
            return loud
        
        for i in range(len(quiet)):
            answer.append(dfs(i,set()))
        return answer
