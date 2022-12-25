class Solution:
    def interpret(self, command: str) -> str:
        res =''
        n = len(command)
        i=0
        for i in range(n):
            if command[i]=='G':
                res+='G'
            elif command[i]==')':
                if command[i-1] == '(':
                    res+='o'
                elif command[i-1]=='l':
                    res+='al'
            else:
                continue      
        return res
                    
                    
                
           
        