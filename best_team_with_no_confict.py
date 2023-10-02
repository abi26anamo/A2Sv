class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pairs = [[ scores[i],ages[i]] for i in range(n)]
        pairs.sort()  

        dp = [pairs[i][0] for i in range(n)]

        for i in range(n):
            for j in range(i):
                if pairs[i][1] >= pairs[j][1]:
                    dp[i] = max(dp[i],dp[j]+pairs[i][0])
                
        return max(dp)
