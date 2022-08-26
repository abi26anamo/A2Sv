class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sort_ed = sorted(str(n))
        s = 1
        while s <=10**9:
            if sorted(str(s)) == sort_ed:
                return True
            s*=2
        return False
