class Solution:
        def __init__(self):
            self.get_str ={}
        def invert(self,s):
            return "".join(["0" if i =="1" else "1" for i in s])
        
            
        def formstr(self,n):
            if n in self.get_str:
                return self.get_str[n]
            if n <=1:
                return "0"
            str_prev = self.formstr(n-1)
            res = f"{str_prev}{'1'}{self.invert(str_prev)[::-1]}"
            self.get_str[n] =res
            return res
        def findKthBit(self, n: int, k: int) -> str:
            s= self.formstr(n)
            return s[k-1]