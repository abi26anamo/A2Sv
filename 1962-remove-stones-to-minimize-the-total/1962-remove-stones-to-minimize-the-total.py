class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap =[-p for p in piles]
        heapq.heapify(max_heap)
     
        while k>0:
            stone = -heapq.heappop(max_heap)
            heapq.heappush(max_heap,-1*stone//2)
            k-=1
        return -sum(max_heap)
        