class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
       visited = set()
       queue = deque()
       def bfs(node):
           queue.append(node)
           while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for i in rooms[node]:
                    queue.append(i)
       bfs(0)
       return len(rooms)==len(visited)
