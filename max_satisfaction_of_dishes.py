class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True) 
        n = len(satisfaction)
        res, pref = 0,0 

        for i in range(n):
            pref+=satisfaction[i]   
            res = max(res,res+pref)
        return res
