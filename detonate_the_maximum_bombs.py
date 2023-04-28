class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #function to check if two bombs are within a range
        def withinRange(b1,b2):
            dist = (b1[0]-b2[0])**2+(b1[1]-b2[1])**2
            return dist<=b1[2]**2
        
        #building graph of bombs with a range
        graph = defaultdict(set)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i!=j and withinRange(bombs[i],bombs[j]):
                    graph[i].add(j)
                    
        

        def dfs(bomb,visited):
            curr_detonated = 1
            visited.add(bomb)
            for bomb2 in graph[bomb]:
                if bomb2 not in visited:
                    curr_detonated+=dfs(bomb2,visited)
            return curr_detonated
            
        max_detonated = 0
        for i in range(len(bombs)):
                max_detonated = max(max_detonated,dfs(i,set()))

        return max_detonated
