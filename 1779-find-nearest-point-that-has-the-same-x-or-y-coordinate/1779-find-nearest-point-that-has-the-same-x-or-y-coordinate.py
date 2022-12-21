class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mindist= float('inf')
        index =-1
        for i ,v in enumerate(points):
            if v[0]==x or v[1]==y:
                minm = abs(x-v[0])+abs(v[1]-y)
                if (mindist>minm):
                    mindist = minm
                    index =i
        return index
            
     
       
           
