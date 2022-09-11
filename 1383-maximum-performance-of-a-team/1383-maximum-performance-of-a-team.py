class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        temp = zip(efficiency,speed)
        temp = sorted(temp)
        res =0
        heap = []
        sm =0
        for i in range(n-1,-1,-1):
            heapq.heappush(heap,temp[i][1])
            sm+=temp[i][1]
            if len(heap)>k:
                sm-=heapq.heappop(heap)
            res =max(res,sm*temp[i][0])
        return res %(10**9+7)
        