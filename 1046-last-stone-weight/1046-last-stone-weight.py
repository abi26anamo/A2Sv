class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-val for val in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x,y  = heapq.heappop(heap),heapq.heappop(heap)
            if x !=y:
                heapq.heappush(heap,x-y)
        if len(heap) ==0:
            return 0
        else:
            return -heap[0]
        
