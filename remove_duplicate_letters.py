class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        hash_set = set()
        freq = Counter(s)
        
        for i in range(n):
            
            while stack and ord(stack[-1])>ord(s[i]) and freq[stack[-1]]>0 and s[i] not in hash_set:
                hash_set.remove(stack[-1])
                stack.pop()
        
            if s[i] not in hash_set:  
                stack.append(s[i])
                hash_set.add(s[i])
                freq[s[i]]-=1
            else:
                freq[s[i]]-=1
        return "".join(stack)
