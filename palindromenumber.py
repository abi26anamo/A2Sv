 def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i=0
        l = len(x)-1
        while i<=l:
             if x[i]!=x[l]:
                 return False
             i+=1
             l-=1
        return True
        
       
