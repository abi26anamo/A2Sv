class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap =[]
        for word,freq in count.items():
            heapq.heappush(heap,(-freq,word))
        res = []
        while k>0:
            freq,val = heapq.heappop(heap)
            res.append(val)
            k-=1
        return res
        
