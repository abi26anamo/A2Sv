class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minheap =[]
        for num in arr:
            dist = abs(num-x)
            heapq.heappush(minheap,(dist,num))
        kclosest =[]
        while k>0:
            dist,num = heapq.heappop(minheap)
            kclosest.append(num)
            k-=1
        return sorted(kclosest)
            
        