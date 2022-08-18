class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(lambda:[])
        
        for time in times:
            graph[time[0]].append((time[2],time[1]))
        heap = [(0,k)]
        seen = set()
        while heap:
            dist,top = heappop(heap)
            if top in seen:
                continue
            seen.add(top)
            
            if len(seen) == n:
                return dist
            for child in graph[top]:
                if child in seen:
                    continue
                heappush(heap,(dist+child[0],child[1]))
        return -1
        
        
        
        
        
        
