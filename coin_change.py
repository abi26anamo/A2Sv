class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(target):
            if target ==0:
                return 0
            if target <0:
                return inf
            if target in memo:
                return memo[target]
                
            num_steps = inf
            for coin in coins:
                curr_state = target - coin
    
                num_steps = min(num_steps,1+dp(curr_state))
            
            memo[target] = num_steps
            return num_steps  
        return dp(amount) if dp(amount)!=inf else -1           

       
