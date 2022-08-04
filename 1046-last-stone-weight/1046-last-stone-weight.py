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
        
#         # invert the value of the keys and use heapq 
#         # so that we can get max-heap
#         heap = [-x for x in stones]
#         heapify(heap)
        
#         # smash stones
#         while len(heap) > 1:                       
#             x, y = heappop(heap), heappop(heap)     # get the heaviest two stones
#             if x != y:
#                 heappush(heap, x - y)               # store the new weight back to the heap
                
#         # check if there is remaining stone 
#         if len(heap) == 0: return 0
#         else: return -heap[0] 