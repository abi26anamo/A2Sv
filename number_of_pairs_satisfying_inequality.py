class Solution:
   def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
       self.count =0
       nums = [nums1[i]-nums2[i] for i in range(len(nums1))]

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
           
       def binarySearch(arr,target):
           l,r = -1,len(arr)
           while l+1 <r:
               mid = (l+r)//2
               if arr[mid]>=target:
                   r = mid
               else:
                   l = mid
           return r

       def mergesort(arr):
           if len(arr)==1:
              return arr
           mid = len(arr)//2
           left = mergesort(arr[:mid])
           right = mergesort(arr[mid:])
           
           for i in left:
               val =binarySearch(right,i-diff)               
               self.count+=(len(right)-val)
           return merge([],left,right)
       mergesort(nums)
       return self.count
