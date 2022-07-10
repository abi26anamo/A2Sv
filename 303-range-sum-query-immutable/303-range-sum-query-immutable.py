class NumArray:

    def __init__(self, nums: List[int]):
        self.cum = [0]
        for num in nums:
            self.cum+=[self.cum[-1]+num]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.cum[right+1] - self.cum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)