class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0 or x ==1:
            return x
        ans =1
        s =1
        while ans <=x:
            s+=1
            ans = s*s
        return s-1
        