class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        
        contains = False
        while right <=len(s2):
            if sorted(s2[left:right]) ==sorted(s1):
                contains = True
                break
            left+=1
            right+=1
        return contains
