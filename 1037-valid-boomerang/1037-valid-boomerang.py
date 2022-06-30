class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        one,two,three = points
        if (two[1]-one[1])*(three[0]-two[0]) == (two[0]-one[0])*(three[1]-two[1]):
            return False
        return True
        
        