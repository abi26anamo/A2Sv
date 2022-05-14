class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(list(s))
        
        for i in range(len(s)):
            if counter.get(s[i]) ==1:
                return i
        return -1
            