class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
       heap = []

       for pile in piles:
           heapq.heappush(heap,-pile)
       
       while k>0:
           curr = heapq.heappop(heap)
           curr = (-1*curr) - ((-1*curr)//2)
           heapq.heappush(heap,-curr)
           k-=1
       return -sum(heap)

