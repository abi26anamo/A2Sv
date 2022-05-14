class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            s = "".join(sorted(str(num)))
            if s[0] == "0":
                for i in range(len(s)):
                    if s[i]!="0":
                        return s[i] + s[:i] + s[i+1:]
            return int(s)
        elif num == 0:
            return 0
        
        else:
            s="".join(sorted(str(num)[1:],reverse= True))
            return -int(s)
        