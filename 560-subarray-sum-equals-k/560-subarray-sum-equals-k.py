class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out =0
        cur = 0
        psum = {0:1}
        for n in nums:
            cur+=n
            dif = cur-k
            out+=psum.get(dif,0)
            psum[cur]=1+psum.get(cur,0)
        return out
        