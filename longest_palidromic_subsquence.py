class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp =[[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
            
        for start in range(n-2,-1,-1):
            for end in range(start+1,n):
                if s[start] == s[end]:
                    dp[start][end] = 2+dp[start+1][end-1]
                else:
                    dp[start][end] = max(dp[start+1][end] ,dp[start][end-1])
        return dp[0][n-1]
        
