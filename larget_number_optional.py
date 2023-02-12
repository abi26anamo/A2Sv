class Solution:
    def largestNumber(self, nums: List[int]) -> str:
              
                nums = map(str,nums)
                def comp(a,b):
                    if a+b >b+a :
                        return -1
                    elif a+b < b+a:
                        return 1
                    else:
                        return 0
                   
                nums = sorted(nums,key = functools.cmp_to_key(comp))
                return str(int("".join(nums)))
