class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources =set()
        sinks =set()
        for source,sink in edges:
            sources.add(source)
            sinks.add(sink)
        res = []
        for val in sources:
            if val not in sinks:
                res.append(val)
        return res

        
       
