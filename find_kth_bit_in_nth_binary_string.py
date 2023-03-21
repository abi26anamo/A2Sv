class Solution:
        def __init__(self):
            pass
        def invert(self,s):
            return "".join(["0" if i =="1" else "1" for i in s])
        def formstr(self,n):
            if n==1:
                return "0"
            return f"{self.formstr(n-1)}{'1'}{self.invert(self.formstr(n-1))[::-1]}"

        def findKthBit(self, n: int, k: int) -> str:
            res = self.formstr(n)
            return res[k-1]
            
