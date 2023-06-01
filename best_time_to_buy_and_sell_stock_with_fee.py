class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i,have):
            if i == len(prices):
                return 0
            if (i,have) in memo:
                return memo[(i,have)]

            if have:
                sell = prices[i]-fee +dp(i+1,not have)
                not_sell = dp(i+1,have)
                memo[(i,have)] = max(sell,not_sell)
                return max(sell,not_sell)
            else:
                buy = dp(i+1,not have)-prices[i]
                not_buy = dp(i+1,have)
                memo[(i,have)] = max(buy,not_buy)
                return max(buy,not_buy)
        return  dp(0,False)
