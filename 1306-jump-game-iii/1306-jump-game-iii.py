class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = collections.deque()
        queue.append(start)
        cached = set()
        
        while queue:
            indx = queue.popleft()
            if arr[indx]==0:
                return True
            for x in (indx+arr[indx],indx-arr[indx]):
                if 0<= x <len(arr) and x not in cached:
                    queue.append(x)
                    cached.add(indx)
        return False