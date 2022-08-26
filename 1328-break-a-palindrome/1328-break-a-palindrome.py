class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<=1:
            return ""
        p=list(palindrome)
        mid = len(p)//2
        for i in range(mid):
            if p[i]!="a":
                p[i]="a"
                return "".join(p)
            
        p[-1]="b"
        return "".join(p)
        
        