class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9+7
        top = pow(2,p,mod)-1
        mid = top-1
        midcount=pow(2,p-1)-1
        return (pow(mid,midcount,mod)*top)%mod
        