class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        visited = set()

        for u,v in adjacentPairs:
            adj_graph[u].append(v)
            adj_graph[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        
        for key in adj_graph.keys():
            if indegree[key]==1:
                queue.append(key)
                visited.add(key)
                break
    
        res = []
        while queue:
            curr_node = queue.popleft()
            res.append(curr_node)

            for neighbor in adj_graph[curr_node]:
                indegree[neighbor]-=1

                if neighbor not in visited and indegree[neighbor]<=1:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return res
