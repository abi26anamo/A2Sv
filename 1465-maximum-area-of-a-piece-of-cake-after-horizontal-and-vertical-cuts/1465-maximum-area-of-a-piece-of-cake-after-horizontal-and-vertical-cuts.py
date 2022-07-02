class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horcut = [0]+horizontalCuts+[h]
        vercut = [0]+verticalCuts+[w]
        maxh = 0
        maxw = 0
        for i in range(1,len(horcut)):
            maxh = max(maxh,horcut[i]-horcut[i-1])
        for j in range(1,len(vercut)):
            maxw = max(maxw,vercut[j]-vercut[j-1])
        return (maxh*maxw)%(10**9+7)
