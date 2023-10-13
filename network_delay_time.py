class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        queue = [(0,k)] 
        visited =set() 
        min_delay = 0
        while queue:
            curr_time,node = heapq.heappop(queue) 
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return curr_time
            for neigh,neigh_time in graph[node]:
                time = neigh_time+curr_time
                if neigh not in visited:
                    heapq.heappush(queue, (time,neigh))
        return  -1
