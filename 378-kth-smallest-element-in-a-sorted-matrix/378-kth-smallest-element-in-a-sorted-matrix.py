class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        maxH = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(maxH, -matrix[i][j])
                if len(maxH) > k:
                    heapq.heappop(maxH)
        return -maxH[0]
 
        