class Solution:
    def similarPairs(self, words: List[str]) -> int:
        unique =[]
        res=0
        for w in words:
            ch = ''.join(sorted(frozenset(w)))
            unique.append(ch)
        count = Counter(unique)
        for item,val in count.items():
            res+=val*(val-1)//2
        return res
            
           
                         