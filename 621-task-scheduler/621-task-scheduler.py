class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counters = {}
        maxcount = 0
        
        for task in tasks:
            counters[task] = counters.get(task, 0) + 1
            maxcount = max(counters[task], maxcount)
                
        numOfMax = 0
    
        for value in counters.values():
            if value == maxcount:
                numOfMax += 1

        numOfChunks = maxcount - 1
        chunkSize = n + 1        
        
        sizeOfAllChunks = numOfChunks * chunkSize + numOfMax
        
        return max(len(tasks), sizeOfAllChunks)
        