class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count=0
        def merge(merged,l_arr,r_arr):
           i =0
           j =0
           while i < len(l_arr) and j < len(r_arr):
               if l_arr[i]<=r_arr[j]:
                   merged.append(l_arr[i])
                   i+=1 
               else:
                   merged.append(r_arr[j])
                   j+=1
           while i < len(l_arr):
               merged.append(l_arr[i])
               i+=1
           while j < len(r_arr):
               merged.append(r_arr[j])
               j+=1
           return merged

        def mergesort(arr):
           if len(arr)==1:
              return arr

           mid = len(arr)//2
           left = mergesort(arr[:mid])
           right = mergesort(arr[mid:])

           for i in left:
               val =bisect_left(right,i/2)               
               self.count+=val
           return merge([],left,right)

        mergesort(nums)
        return self.count
