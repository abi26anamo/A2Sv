class Solution:
   def countSmaller(self, nums: List[int]) -> List[int]:
       self.count =defaultdict(int)
       
       def merge(merged,l_arr,r_arr):
           i =0
           j =0
           while i < len(l_arr) and j < len(r_arr):
               if nums[l_arr[i]]<=nums[r_arr[j]]:
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
           left,right = -1,len(arr)
           while left+1 <right:
               mid = (left+right)//2
               if arr[mid]>=target:
                   right = mid
               else:
                   left = mid
           return right

       def mergesort(arr):
           if len(arr)==1:
              return arr

           mid = len(arr)//2
           left = mergesort(arr[:mid])
           right = mergesort(arr[mid:])
           right_arr_values = [nums[i] for i in right]

           for i in left:
               val =binarySearch(right_arr_values,nums[i])               
               self.count[i]+=val
           return merge([],left,right)

       mergesort([i for i in range(len(nums))])

       return [self.count[i] for i in range(len(nums))]
