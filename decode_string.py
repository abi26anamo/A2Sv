class Solution:
    def decodeString(self, s: str) -> str:
        k=0
        cur =""
        stack=[]
        for c in s:
            if c.isdigit():
                k=k*10 +int(c)
            if c.isalpha():
                cur+=c
            if c=="[":
                stack.append((cur,k))
                k=0
                cur=""
            if c =="]":
                last_c,last_k =stack.pop(-1)
                cur = last_c+last_k*cur
        return cur
