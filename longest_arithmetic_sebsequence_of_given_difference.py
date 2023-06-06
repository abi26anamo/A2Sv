class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        memo = {}
        for i in range(n):
            prev = arr[i]-difference
            if prev in memo:
                memo[arr[i]] = 1+memo[prev]
            else:
                memo[arr[i]] = 1

        max_val  =0
        for val in memo.values():
            max_val = max(max_val,val)
        return max_val
