class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = [(st,pt,idx) for idx,(st,pt) in enumerate(tasks)]
        tasks.sort()
        
        i = 0
        heap = []
        res =[]
        time = tasks[0][0]
    
        while len(res)!=len(tasks):
            while i <len(tasks) and tasks[i][0]<=time:
                heapq.heappush(heap,(tasks[i][1],tasks[i][2]))
                i+=1
            if heap:
                pt,idx = heapq.heappop(heap)
                res.append(idx)
                time+=pt
            elif i<len(tasks):
                time = tasks[i][0]
        return res
            
                
         
            
                
        
        
        
        
        
        
        