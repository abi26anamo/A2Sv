class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        modified_string = ""
        j=0
        for i in range(len(s)):
            
            if len(spaces)==0:
                return s
            
            if len(spaces)>1 and j<len(spaces) and i==spaces[j] and len(s):
                
                modified_string+=" "
                modified_string+=s[i]
                j+=1
                
            elif len(spaces)==1 and i==spaces[0] and len(s):
                
                modified_string+=" "
                modified_string+=s[i]
                
            elif len(spaces)==1 and i==spaces[0] and len(s)==0:
                modified_string+=" "
                
            else:
                modified_string+=s[i]
    
        return modified_string
                
