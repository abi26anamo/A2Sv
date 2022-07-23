class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(40):
            if n == 2**x:
                return True
                x+=1
        return False