class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        val = float('inf')
        for v in count.values():
            val = min(val,v)
        if val==1:
            return False
        for i in range(2,val+1):
            res = [ct%i for ct in count.values()]
            if sum(res)==0:
                return True
        return False
