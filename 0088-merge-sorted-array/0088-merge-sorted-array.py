class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
      Do not return anything, modify nums1 in-place instead.
        
        """
        i=m
        j=n
        idex = m+n-1
        while i >0 and j >0:
            if nums1[i-1] >= nums2[j-1]:
                nums1[idex] = nums1[i-1]
                i-=1
                idex-=1
            elif nums1[i-1]<nums2[j-1]:
                nums1[idex] = nums2[j-1]
                j-=1
                idex-=1
        while i >0:
            nums1[idex]=nums1[i-1]
            i-=1
            idex-=1
        while j>0:
            nums1[idex]=nums2[j-1]
            j-=1
            idex-=1
       