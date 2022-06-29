class Solution:
    def calculate(self, s: str) -> int:
        num=0
        sign ="+"
        stack =[]
        for v in s+"+":
            if v.isdigit():
                num= num*10 + int(v)
            elif v in "+-*/":
                if sign =="+":
                    stack.append(num)
                elif sign =="-":
                    stack.append(-num)
                elif sign =="*":
                    stack.append(stack.pop()*num)
                elif sign =="/":
                    stack.append(math.trunc(stack.pop()/num))
                sign =v
                num=0
        return sum(stack)
                
            
    
        