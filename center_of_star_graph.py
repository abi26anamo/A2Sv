class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = defaultdict(int)
        for u,v in edges:
            count[u]+=1
            count[v]+=1                
        for val in count:
            if count[val]==len(edges):
                return val
