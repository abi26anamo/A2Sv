class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0

        memo = [0] * n

        memo[0] = 1

        for i in range(1,n):
            if s[i-1] != '0' and int(s[i-1:i+1])<=26:
                if s[i] != '0' and i>=2:
                    memo[i] = memo[i-1]+memo[i-2]
                elif s[i] != '0' and i<2:
                    memo[i] = memo[i-1]+1
                else:
                    if i>=2:
                        memo[i] = memo[i-2]
                    else:
                        memo[i] =1
            elif s[i-1] != '0' and s[i] =='0' and int(s[i-1:i+1])>26:
                return 0
            elif s[i-1] =='0' and s[i] == '0':
                return 0
            else:
                memo[i] = memo[i-1]
            
        return memo[-1]            
                



