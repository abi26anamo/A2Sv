class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur =0
        hst =0
        for i in gain:
            cur+=i
            hst =max(hst,cur)
        return hst
        