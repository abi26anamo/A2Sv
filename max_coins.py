class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        j= n-2
        total_coins =0
        for i in range(n//3,0,-1):
            total_coins+=piles[j]
            j-=2
        return total_coins
