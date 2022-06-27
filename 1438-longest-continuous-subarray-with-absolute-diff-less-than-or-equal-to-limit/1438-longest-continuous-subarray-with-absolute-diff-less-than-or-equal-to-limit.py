from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        largest = deque()
        smallest = deque()
        n= len(nums)
        i=0
        j=0
        k=0
        while j <n:
            val = nums[j]
            while largest and largest[-1] <val:
                largest.pop()
            largest.append(val)
            while smallest and smallest[-1] >val:
                smallest.pop()
            smallest.append(val)
            while largest[0]-smallest[0] >limit:
                if largest[0]==nums[i]:
                    largest.popleft()
                if smallest[0]== nums[i]:
                    smallest.popleft()
                i+=1
                
            k= max(k,j-i+1)
            j+=1
        return k