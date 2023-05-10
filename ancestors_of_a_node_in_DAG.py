class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        ancestors = [[] for _ in range(n)]
        queue = deque()
        for source,dest in edges:
            graph[source].append(dest)
            ancestors[dest]+=[source]
            indegree[dest]+=1

        print(graph)
        print(ancestors)
        for i in range(n):
           if indegree[i]==0:
               queue.append(i)
        
        while queue:
            node = queue.popleft()
            ancestors[node] =sorted(set(ancestors[node]))
            for neighbor in graph[node]:
                ancestors[neighbor]+=[node]
                ancestors[neighbor]+=ancestors[node]
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return  ancestors
            


