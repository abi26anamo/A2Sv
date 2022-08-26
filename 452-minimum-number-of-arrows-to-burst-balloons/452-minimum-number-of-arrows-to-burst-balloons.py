class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows=1
        temp= points[0]
        for start,end in points[1:]:
            if start > temp[1]:
                arrows+=1
                temp = [start,end]
            else:
                temp[1]= min(temp[1],end)
        return arrows
    


