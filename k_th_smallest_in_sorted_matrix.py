class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n= len(matrix)
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap,matrix[i][j])
 
        while k>1:
            heapq.heappop(heap)
            k-=1
        return heap[0]
