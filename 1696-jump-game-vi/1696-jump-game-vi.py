from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        arr =[0]*n
        arr[0]=nums[0]
        q= deque([(nums[0],0)])
        for i in range(1,n):
            arr[i]=nums[i]+q[0][0]
            while q and q[-1][0]<arr[i]:
                q.pop()
            q.append((arr[i],i))
            if i-k == q[0][1]:
                q.popleft()
        return arr[-1]