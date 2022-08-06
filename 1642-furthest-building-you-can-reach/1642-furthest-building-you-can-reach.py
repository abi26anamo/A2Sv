class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxheap = []
        for i in range(len(heights)-1):
            jump = heights[i+1] - heights[i]
            if jump <=0:
                continue
            heapq.heappush(maxheap,-jump)
            bricks-=jump
            if bricks <0 and ladders ==0:
                return i 
            if bricks <0:
                ladders-=1
                bricks-=heapq.heappop(maxheap)
        return len(heights)-1