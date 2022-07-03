class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_len = [len(elem) for elem in strs]
        min_len = min(strs_len)
        
        strs = [elem[0:min_len] for elem in strs]
        
        while strs:
            print(strs)
            if len(set(strs)) <= 1:
                return strs[0]
            else:
                strs = [elem[0:len(elem)-1] for elem in strs]