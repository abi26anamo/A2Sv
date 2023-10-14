class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list) 
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0],1/values[i]))
        
        def bfs(src,des):
            queue = deque()
            visited = set() 

            if src not in graph or des not in graph:
                return -1

            queue.append((src,1)) 
            visited.add(src)  

            while queue:
                node,curr_w = queue.popleft() 
                if node == des:
                    return curr_w 
                
                for neighbor,weight in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor,weight*curr_w))
                        visited.add(neighbor)   
            return -1
        res = []   
        for query in queries:
            curr = bfs(query[0],query[1]) 
            res.append(curr) 
        return res
