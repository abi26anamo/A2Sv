class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree=defaultdict(int)
        queue= deque()
        order = []

        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            for neighbor in graph[course]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        if len(order)!=numCourses:
            return False
        return True


        
       

