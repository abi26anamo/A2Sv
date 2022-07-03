class Solution:
        def help(self,s,l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        def longestPalindrome(self, s: str) -> str:
            l_pali =""
            for i in range(len(s)):
                curr = ""
                odd=self.help(s,i,i)
                even = self.help(s,i,i+1)
                if len(s) <= 1:
                    return s
                if len(odd)>len(even):
                    curr = odd
                else:
                    curr = even
                if len(curr) > len(l_pali):
                    l_pali = curr

            return l_pali