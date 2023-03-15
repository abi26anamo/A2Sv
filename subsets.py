class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(idx,given_arr,ans,curr_arr):
            if idx==len(given_arr):
                ans.append(curr_arr[:])
                return ans
            curr_arr.append(given_arr[idx])
            helper(idx+1,given_arr,ans,curr_arr)
            curr_arr.pop()
            helper(idx+1,given_arr,ans,curr_arr)
            return ans
        return helper(0,nums,[],[])
