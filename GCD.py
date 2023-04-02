class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a= max(nums)
        b = min(nums)
        def func(x,y):
            if y==0:
                return x
            return func(y,x%y)
        return func(a,b)
