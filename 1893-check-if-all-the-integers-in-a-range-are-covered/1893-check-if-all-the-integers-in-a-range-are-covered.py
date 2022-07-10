class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cum = [False]*55
        for s,e in ranges:
            for x in range(s,e+1):
                cum[x] = True
                
        for x in range(left,right+1):
            if not cum[x]:
                return False
        return True
                
            