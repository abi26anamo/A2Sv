class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        oper =0
        pair = set()
        for x in count:
            if x not in pair and (k-x) in count:
                if (k-x)==x:
                    oper+=count[x]//2
                else:
                    oper+=min(count[x],count[k-x])
                    pair.add(x)
                    pair.add(k-x)
        return oper
                
        