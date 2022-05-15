class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        def isnum(num):
            try:
                int(num)
                return True
            except:
                return False
        for t in tokens:
            if isnum(t):
                stack.append(t)
            else:
                a= int(stack.pop())
                b= int(stack.pop())
                if t =="+":
                    c= a+b
                elif t == "-":
                    c=b-a
                elif t=="*":
                    c= a*b
                elif t == "/":
                    c= int(b/a)
                
                stack.append(str(c))
        return stack[-1]