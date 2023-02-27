class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_window = 0
        count = {}
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]]=1
         
            most_frequent = max(count.values())
            while most_frequent+k < right-left+1:
                count[s[left]]-=1
                left+=1
            max_window = max(max_window,right-left+1)
          
        return max_window
