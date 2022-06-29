class Solution:
    def calculate(self, s: str) -> int:
        res =0
        cur =0
        sign =1
        stack=[]
        for c in s:
            if c.isdigit():
                cur = cur*10 +int(c)
                
            elif c in "+-":
                res+=(cur*sign)
                cur=0
                if c == "-":
                    sign= -1
                else:
                    sign=1
            elif c =="(":
                stack.append(res)
                stack.append(sign)
                sign=1
                res=0
            elif c == ")":
                res+=(cur*sign)
                res*=stack.pop()
                res+=stack.pop()
                cur=0
        return res+(cur*sign)
        
        