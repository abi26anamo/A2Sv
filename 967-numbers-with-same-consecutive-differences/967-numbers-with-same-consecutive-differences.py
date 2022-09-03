class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        output =[]
        q = deque()
        for i in range(10):
            q.append([i])
        while q:
            l = q.popleft()
            if len(l)==n:
                l=[str(d) for d in l]
                num=int("".join(l))
                if len(str(num))==n:
                    output.append(num)
            else:
                nx = l[-1]-k
                if 0 <=nx<10:
                    q.append(l+[nx])
                nx = l[-1]+k
                if 0 <=nx<10:
                    q.append(l+[nx])
                    
        return list(set(output))
                    
        