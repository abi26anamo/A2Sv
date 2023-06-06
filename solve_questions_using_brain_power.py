class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        
        def dp(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            solve =  questions[i][0] + dp(i + questions[i][1] + 1) 
            skip = dp(i + 1)
            
            memo[i] = max(solve, skip)
            return memo[i]
        
        return dp(0)
