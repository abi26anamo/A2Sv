class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen ={}
        start =0
        max_len =0
        for i in range(0,len(s)):
            if s[i] in seen:
                start = max(start,seen[s[i]]+1)
            max_len = max(max_len,i-start+1)
            seen[s[i]] =i
        return max_len
     
            
        