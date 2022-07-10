class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q=k%len(nums)
        temp = nums[-q:]
        del nums[-q:]
        nums[:0]+=temp
        
        
        