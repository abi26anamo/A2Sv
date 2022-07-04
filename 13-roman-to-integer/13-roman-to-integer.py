class Solution:
    def romanToInt(self, s: str) -> int:
        dic= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans=0
        l= list(s)
        for i in l:
            ans+=dic[i]
        for i in range(0,len(l)-1):
            if(dic[l[i]]<dic[l[i+1]]):
                ans-= 2*(dic[l[i]])
        return ans
        