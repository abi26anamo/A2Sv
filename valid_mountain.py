class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i=0
        left = 0
        right = len(arr)-1
        
        while left<len(arr)-1:
            if arr[left]<arr[left+1]:
                left+=1
            else:
                break
        while right>0:
            if arr[right]<arr[right-1]:
                right-=1
            else:
                break
        
        return left==right and left!=0 and right!=len(arr)-1
