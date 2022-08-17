class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = []
        q.append(beginWord)
        res = 0
        wordList = set(wordList)
        
        #BFS
        while q:
            res += 1
            qsize = len(q)
            for k in range(qsize):
                word = q.pop(0)
                #If word is result
                if word == endWord:
                    return res
                for i in range(len(word)):
                    start = ord('a')
                    for j in range(26):
                        temp = word[:i] + chr(start+j) + word[i+1:]
                        if (temp in wordList):
                            q.append(temp)
                            wordList.remove(temp)
        return 0
        