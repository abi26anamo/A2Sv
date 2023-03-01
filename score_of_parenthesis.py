class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n= len(s)
        stack = []
        
        for i in range(n):
            if s[i]=="(":
                stack.append(s[i])
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                    curr = 1
                    if not stack or stack[-1]=="(":
                        stack.append(curr)
                    elif stack and stack[-1]!="(":
                        curr+=stack.pop()
                        stack.append(curr)
                else:
                    curr = 2*stack.pop()
                    stack.pop()
                    if not stack or stack[-1]=="(":
                        stack.append(curr)
                    else:
                        curr+=stack.pop()
                        stack.append(curr)
                    
        return stack[0]
                        
                
