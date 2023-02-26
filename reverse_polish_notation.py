class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        def isnum(num):
            try:
                int(num)
                return True
            except:
                return False
        for token in tokens:
            if isnum(token):
                stack.append(int(token))
            else:
                top= stack.pop()
                second_top= stack.pop()
                if token =="+":
                    operation_result= top+second_top
                elif token == "-":
                    operation_result=second_top-top
                elif token=="*":
                    operation_result= top*second_top
                elif token == "/":
                    operation_result= int(second_top/top)
                
                stack.append(operation_result)
        return stack[-1]
