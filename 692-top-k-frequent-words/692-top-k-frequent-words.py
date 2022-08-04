class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        count = Counter(words)
        max_heap =[]
        for key,value in count.items():
             heapq.heappush(max_heap,(-value,key))
        while k >0:
            res.append(heapq.heappop(max_heap)[1])
            k-=1
        return res