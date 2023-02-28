class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurs(x,n):
            if n ==0:
                return 1
            if n ==1:
                return x
            mid = n//2
            return recurs(x,mid)*recurs(x,n-mid)
        return recurs(x,n) if n >0 else 1/recurs(x,abs(n))
