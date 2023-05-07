class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks = [(start_time,process_time,idx) for idx,(start_time,process_time) in enumerate(tasks)]
        tasks.sort()
        print(tasks)
        order =[]
        heap = []
        initial_start = tasks[0][0]
        i =0
        while len(order)!=len(tasks):
            while i < len(tasks) and  tasks[i][0]<=initial_start:
                _, p_time,idx = tasks[i]
                heapq.heappush(heap,(p_time,idx))
                i+=1

            if heap:
                p_time,idx = heapq.heappop(heap)
                order.append(idx)
                initial_start+=p_time
                
            elif i< len(tasks):
                initial_start = tasks[i][0]

        return order



            

            

        



            

       
    

       

        
       
