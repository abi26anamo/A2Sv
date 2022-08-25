class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic={}
        for letter in magazine:
            if letter not in dic:
                dic[letter] = 1 
            else:
                dic[letter] += 1
        for letter in ransomNote:
            if letter not in dic:
                return False
            elif dic[letter]>0:
                dic[letter] -= 1
            else:
                return False
        return True