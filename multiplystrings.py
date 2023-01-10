class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        first_num =0
        for i in num1:
            first_num = first_num*10+(ord(i)-ord('0'))
            
        second_num =0
        for i in num2:
            second_num = second_num*10+(ord(i)-ord('0'))
            
        return str(first_num*second_num)
