class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        n = len(source)
        stack =[]
        res =''
        in_multiline = False
        for line in source:
            i=0
            len_line = len(line)
            while i<len(line):
                char = line[i]
                if char =="/" and i+1 <len_line and line[i+1]=='/' and not in_multiline:
                    i= len(line)
                elif char =="/" and i+1 <len_line and line[i+1]=='*' and not in_multiline:
                    in_multiline = True
                    i+=1
                elif char =="*" and i+1 <len_line and line[i+1]=='/' and in_multiline:
                    in_multiline = False
                    i+=1
                elif not in_multiline:
                    res+=char
                i+=1
            if not in_multiline and res:
                stack.append(res)
                res =''
        return stack
            
        
                    
                    