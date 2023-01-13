class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        def ArrayBuilder(word):
            frequency = [0]*26
            for ch in word:
                frequency[ord(ch)-ord('a')]+=1
            return frequency
        
        for i in range(len(words)):
            words[i]=ArrayBuilder(words[i])

        common_characters = []
        for i in range(26):
            minimum = float('inf')
            for j in range(len(words)):
                minimum = min(minimum,words[j][i])
                
            common_characters+=[chr(i+ord('a'))]*minimum
                    
        return common_characters
                
