class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        def backtrack(curr_comb):
            if len(curr_comb) == 1:
                return [curr_comb]

            ans = []
            for i in range(len(curr_comb)):
                taken = curr_comb[i]
                remaining = curr_comb[:i]+curr_comb[i+1:]
                backtracked  = backtrack(remaining)
                for j in backtracked:
                    ans.append(j+[taken])
            return ans
            
        return backtrack(nums)
