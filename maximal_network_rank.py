class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        max_len =0
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        rank =0
        for i in range(n):
            for j in range(i+1,n):
                rank = len(graph[i])+len(graph[j])
                if i in graph[j] or j in graph[i]:
                    rank-=1
                max_len = max(rank,max_len)
        return max_len
                
