class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(start,end,st):
            if start>=end:
                return 
            s[start],s[end] = s[end],s[start]
            helper(start+1,end-1,st)
        helper(0,len(s)-1,s)
        return s
