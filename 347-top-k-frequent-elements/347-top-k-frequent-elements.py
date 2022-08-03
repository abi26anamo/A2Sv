class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        arr =[]
        for num,count in c.items():
            heapq.heappush(arr,(-count,num))
        ans = []
        for _ in range(k):
            _,num = heapq.heappop(arr)
            ans.append(num)
        
        return ans
        
        
        
        
        
#         c= Counter(nums)
#         c= sorted(c,key = lambda x:c[x] ,reverse = True)
        
#         return c[:k]
          