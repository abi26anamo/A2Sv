class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                  "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                  "..-","...-",".--","-..-","-.--","--.."]
    
        def transform(word):
            morse = ''
            for letter in word:
                morse+=morse_list[ord(letter)-97]
            return morse

        ans = set()
        for word in words:
            ans.add(transform(word))

        return len(ans)
        