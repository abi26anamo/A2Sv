class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = {node:float(inf) for node in range(n)}
        distance[src] = 0
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))
        
        queue = [(0, 0, src)]

        while queue:
            cur_k, cur_w, u = heapq.heappop(queue)
            for v, w in graph[u]:
                weight = cur_w + w
                if weight < distance[v] and cur_k <= k:
                    heapq.heappush(queue, (cur_k + 1, weight, v))
                    distance[v] = weight
        
        return distance[dst] if distance[dst]!= float(inf) else -1  
