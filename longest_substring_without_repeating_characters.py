class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        left=0
        max_len = 0

        for right in range(len(s)):
            
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
                
            hash_set.add(s[right])
            
            max_len = max(right-left+1, max_len)
                
        return max_len   
     
