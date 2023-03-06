class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f_query = []
        res = []
        for query in queries:
            count_query = Counter(query)
            curr_query = sorted(query)
            f_query.append(count_query[curr_query[0]])

        f_words = []
        for word in words:
            count_word = Counter(word)
            curr_word = sorted(word)
            f_words.append(count_word[curr_word[0]])
        f_words.sort()
        for i in range(len(queries)):
            left,right = -1,len(words)
            while left+1 < right:
                mid = left+(right - left)//2

                if f_words[mid] <= f_query[i]:
                    left = mid
                else:
                    right = mid
            res.append(len(words)-right)
        return res
